from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Avg, Count, Q
from django.http import FileResponse
import pandas as pd
import io
from .models import Equipment, UploadBatch
from .serializers import (
    UserSerializer, EquipmentSerializer, UploadBatchSerializer, 
    CSVUploadSerializer, SummarySerializer
)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """User login endpoint"""
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': UserSerializer(user).data
    })

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """User registration endpoint"""
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email)
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'token': token.key,
        'user': UserSerializer(user).data
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    """Upload and process CSV file"""
    if 'file' not in request.FILES:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    file = request.FILES['file']
    
    try:
        # Read CSV file
        df = pd.read_csv(file)
        
        # Validate required columns
        required_columns = ['Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature']
        if not all(col in df.columns for col in required_columns):
            return Response(
                {'error': f'CSV must contain columns: {", ".join(required_columns)}'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Create upload batch
        batch = UploadBatch.objects.create(
            user=request.user,
            filename=file.name,
            total_equipment=len(df)
        )
        
        # Process each row
        for idx, row in df.iterrows():
            Equipment.objects.create(
                batch=batch,
                equipment_name=str(row['Equipment Name']).strip(),
                equipment_type=str(row['Type']).strip(),
                flowrate=float(row['Flowrate']),
                pressure=float(row['Pressure']),
                temperature=float(row['Temperature'])
            )
        
        # Calculate statistics
        stats = Equipment.objects.filter(batch=batch).aggregate(
            avg_flowrate=Avg('flowrate'),
            avg_pressure=Avg('pressure'),
            avg_temperature=Avg('temperature')
        )
        
        batch.avg_flowrate = stats['avg_flowrate'] or 0
        batch.avg_pressure = stats['avg_pressure'] or 0
        batch.avg_temperature = stats['avg_temperature'] or 0
        batch.save()
        
        # Clean up old batches (keep only last 5)
        old_batches = UploadBatch.objects.filter(user=request.user).order_by('-created_at')[5:]
        for old_batch in old_batches:
            old_batch.delete()
        
        return Response(UploadBatchSerializer(batch).data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_summary(request):
    """Get latest upload summary"""
    latest_batch = UploadBatch.objects.filter(user=request.user).first()
    
    if not latest_batch:
        return Response({'error': 'No upload found'}, status=status.HTTP_404_NOT_FOUND)
    
    equipment = Equipment.objects.filter(batch=latest_batch)
    
    # Calculate type distribution
    type_dist = equipment.values('equipment_type').annotate(count=Count('id'))
    equipment_types = {item['equipment_type']: item['count'] for item in type_dist}
    
    # Calculate ranges
    flowrate_stats = equipment.aggregate(min=Avg('flowrate')*0.8, max=Avg('flowrate')*1.2)
    pressure_stats = equipment.aggregate(min=Avg('pressure')*0.8, max=Avg('pressure')*1.2)
    temp_stats = equipment.aggregate(min=Avg('temperature')*0.8, max=Avg('temperature')*1.2)
    
    summary = {
        'total_equipment': equipment.count(),
        'equipment_types': equipment_types,
        'avg_flowrate': latest_batch.avg_flowrate,
        'avg_pressure': latest_batch.avg_pressure,
        'avg_temperature': latest_batch.avg_temperature,
        'flowrate_range': {'min': flowrate_stats['min'], 'max': flowrate_stats['max']},
        'pressure_range': {'min': pressure_stats['min'], 'max': pressure_stats['max']},
        'temperature_range': {'min': temp_stats['min'], 'max': temp_stats['max']},
    }
    
    return Response(summary)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_history(request):
    """Get last 5 uploads"""
    batches = UploadBatch.objects.filter(user=request.user)[:5]
    return Response(UploadBatchSerializer(batches, many=True).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_data(request):
    """Get equipment data from latest upload"""
    latest_batch = UploadBatch.objects.filter(user=request.user).first()
    
    if not latest_batch:
        return Response({'error': 'No upload found'}, status=status.HTTP_404_NOT_FOUND)
    
    equipment = Equipment.objects.filter(batch=latest_batch)
    return Response(EquipmentSerializer(equipment, many=True).data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def download_report(request):
    """Generate PDF report"""
    from reportlab.lib.pagesizes import letter
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from io import BytesIO
    from datetime import datetime
    
    try:
        latest_batch = UploadBatch.objects.filter(user=request.user).first()
        if not latest_batch:
            return Response({'error': 'No upload found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Get summary data
        equipment = Equipment.objects.filter(batch=latest_batch)
        type_dist = equipment.values('equipment_type').annotate(count=Count('id'))
        
        # Create PDF
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()
        
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1a56db'),
            spaceAfter=30,
        )
        
        elements.append(Paragraph('Equipment Analysis Report', title_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Report info
        info_style = styles['Normal']
        elements.append(Paragraph(f'<b>Report Date:</b> {datetime.now().strftime("%Y-%m-%d %H:%M")}', info_style))
        elements.append(Paragraph(f'<b>Upload File:</b> {latest_batch.filename}', info_style))
        elements.append(Paragraph(f'<b>Total Equipment:</b> {equipment.count()}', info_style))
        elements.append(Spacer(1, 0.3*inch))
        
        # Statistics
        elements.append(Paragraph('<b>Summary Statistics</b>', styles['Heading2']))
        stats_data = [
            ['Parameter', 'Value'],
            ['Average Flowrate', f"{latest_batch.avg_flowrate:.2f}"],
            ['Average Pressure', f"{latest_batch.avg_pressure:.2f}"],
            ['Average Temperature', f"{latest_batch.avg_temperature:.2f}"],
        ]
        
        stats_table = Table(stats_data, colWidths=[3*inch, 2*inch])
        stats_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a56db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(stats_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Type distribution
        elements.append(Paragraph('<b>Equipment Type Distribution</b>', styles['Heading2']))
        type_data = [['Equipment Type', 'Count']]
        for item in type_dist:
            type_data.append([item['equipment_type'], str(item['count'])])
        
        type_table = Table(type_data, colWidths=[3*inch, 2*inch])
        type_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a56db')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))
        elements.append(type_table)
        
        doc.build(elements)
        buffer.seek(0)
        
        return FileResponse(
            buffer,
            as_attachment=True,
            filename='equipment_report.pdf',
            content_type='application/pdf'
        )
    
    except Exception as e:
        print(f"[v0] PDF generation error: {str(e)}")
        return Response({'error': f'Failed to generate report: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    """Logout endpoint"""
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'})