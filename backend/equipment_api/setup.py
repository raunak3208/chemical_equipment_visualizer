#!/usr/bin/env python
"""
Automated setup script for Chemical Equipment Parameter Visualizer Backend
Handles database initialization, migrations, and superuser creation
"""

import os
import sys
import django
from pathlib import Path

# Add backend directory to path
sys.path.insert(0, str(Path(__file__).parent))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User

def run_setup():
    """Run complete setup sequence"""
    print("=" * 60)
    print("Chemical Equipment Parameter Visualizer - Backend Setup")
    print("=" * 60)
    
    # Step 1: Run migrations
    print("\n[1/3] Running database migrations...")
    try:
        call_command('migrate', verbosity=1)
        print("✓ Migrations completed successfully")
    except Exception as e:
        print(f"✗ Migration failed: {e}")
        return False
    
    # Step 2: Create superuser if needed
    print("\n[2/3] Creating superuser account...")
    try:
        if User.objects.filter(username='admin').exists():
            print("✓ Admin user already exists")
        else:
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            print("✓ Admin user created")
            print("  Username: admin")
            print("  Password: admin123")
            print("  Note: Change this password in production!")
    except Exception as e:
        print(f"✗ Superuser creation failed: {e}")
        return False
    
    # Step 3: Create uploads directory
    print("\n[3/3] Creating uploads directory...")
    try:
        uploads_dir = Path(__file__).parent / 'uploads'
        uploads_dir.mkdir(exist_ok=True)
        print("✓ Uploads directory ready")
    except Exception as e:
        print(f"✗ Failed to create uploads directory: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("Setup completed successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Start the backend server:")
    print("   python manage.py runserver")
    print("\n2. Access the admin interface at:")
    print("   http://localhost:8000/admin/")
    print("\n3. Use the sample CSV to test:")
    print("   ../data/sample_equipment_data.csv")
    print("=" * 60)
    
    return True

if __name__ == '__main__':
    success = run_setup()
    sys.exit(0 if success else 1)
