# Chemical Equipment Parameter Visualizer

A comprehensive hybrid application for monitoring and analyzing chemical equipment parameters with both web and desktop interfaces.

## Project Architecture

### Technology Stack
- **Backend**: Django + Django REST Framework + SQLite
- **Web Frontend**: React.js + Chart.js + Tailwind CSS
- **Desktop Frontend**: PyQt5 + Matplotlib
- **Additional**: ReportLab (PDF Generation)

### Key Features
- CSV file upload and data processing
- Real-time analytics and statistics
- Multi-format data visualization (charts, tables)
- Historical data tracking (last 5 uploads)
- PDF report generation
- Basic authentication system
- Responsive UI for web and desktop

## Project Structure

\`\`\`
chemical-equipment-visualizer/
├── backend/                    # Django Backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── equipment_api/          # Main Django app
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── config/                 # Django settings
│   └── uploads/                # CSV uploads directory
├── frontend-web/               # React Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── UploadForm.jsx
│   │   │   ├── DataTable.jsx
│   │   │   ├── Charts.jsx
│   │   │   └── History.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── index.css
│   ├── package.json
│   └── vite.config.js
├── frontend-desktop/           # PyQt5 Desktop App
│   ├── main.py
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── upload_dialog.py
│   │   ├── charts_widget.py
│   │   └── history_widget.py
│   ├── services/
│   │   └── api_client.py
│   └── requirements.txt
└── data/
    └── sample_equipment_data.csv
\`\`\`

## Setup Instructions

### Backend Setup

1. **Create virtual environment**:
   \`\`\`bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

2. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run migrations**:
   \`\`\`bash
   python manage.py migrate
   \`\`\`

4. **Create superuser**:
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

5. **Start server**:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

Backend will be available at: `http://localhost:8000`

### Web Frontend Setup

1. **Navigate to frontend-web**:
   \`\`\`bash
   cd frontend-web
   \`\`\`

2. **Install dependencies**:
   \`\`\`bash
   npm install
   # or
   yarn install
   \`\`\`

3. **Start development server**:
   \`\`\`bash
   npm run dev
   \`\`\`

Web app will be available at: `http://localhost:5173`

### Desktop Application Setup

1. **Navigate to frontend-desktop**:
   \`\`\`bash
   cd frontend-desktop
   python -m venv venv
   source venv/bin/activate
   \`\`\`

2. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run application**:
   \`\`\`bash
   python main.py
   \`\`\`

## API Endpoints

### Authentication
- **POST** `/api/auth/login/` - User login
- **POST** `/api/auth/logout/` - User logout

### Equipment Data
- **POST** `/api/upload/` - Upload and process CSV file
- **GET** `/api/summary/` - Get latest processed summary
- **GET** `/api/history/` - Get last 5 uploads
- **GET** `/api/download-report/` - Download PDF report

## Database Schema

### Equipment Table
\`\`\`sql
CREATE TABLE equipment (
    id INTEGER PRIMARY KEY,
    equipment_name VARCHAR(255),
    type VARCHAR(100),
    flowrate FLOAT,
    pressure FLOAT,
    temperature FLOAT,
    created_at TIMESTAMP,
    upload_batch_id INTEGER FOREIGN KEY
);
\`\`\`

### Upload History Table
\`\`\`sql
CREATE TABLE upload_history (
    id INTEGER PRIMARY KEY,
    filename VARCHAR(255),
    total_equipment INTEGER,
    avg_flowrate FLOAT,
    avg_pressure FLOAT,
    avg_temperature FLOAT,
    created_at TIMESTAMP
);
\`\`\`

## CSV File Format

The uploaded CSV must contain the following columns:
- **Equipment Name** - Identifier for the equipment
- **Type** - Category of equipment (e.g., Pump, Compressor, etc.)
- **Flowrate** - Flow rate parameter (numeric)
- **Pressure** - Pressure parameter (numeric)
- **Temperature** - Temperature parameter (numeric)

Example:
\`\`\`
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-A-001,Centrifugal Pump,1200.5,45.2,65.8
Heat Exchanger-HX-01,Heat Exchanger,850.3,32.1,72.3
\`\`\`

## Authentication

Basic authentication is implemented:
- Username/Password credentials required
- Tokens stored in browser (web) and app memory (desktop)
- User sessions managed by Django

## Data Visualization

### Web Charts (Chart.js)
1. **Bar Chart** - Equipment type distribution
2. **Line Chart** - Average flowrate, pressure, temperature trends
3. **Data Table** - Detailed equipment parameters

### Desktop Charts (Matplotlib)
1. **Pie Chart** - Equipment type distribution
2. **Bar Chart** - Average parameter values
3. **Line Plot** - Historical trends

## PDF Report Generation

Reports include:
- Equipment summary statistics
- Type distribution
- Parameter averages and ranges
- Generated timestamp
- Visual charts

## Features

- Upload CSV files with equipment parameters
- Automatic data validation and processing
- Real-time analytics calculation
- Responsive web interface
- Native desktop application
- History tracking (last 5 uploads)
- PDF report generation
- Authentication and security
- Clean, modular code architecture

## Notes

- Only the last 5 uploads are stored in history
- CSV files are processed asynchronously on upload
- Both web and desktop clients connect to the same backend
- PDF reports are generated on-demand
