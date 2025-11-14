# Chemical Equipment Parameter Visualizer

A comprehensive hybrid application for monitoring and visualizing chemical equipment parameters with both web and desktop interfaces.

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- Git

### Fast Setup (3 commands)

1. **Backend** (Terminal 1)
\`\`\`bash
cd backend
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver
\`\`\`

2. **Web Frontend** (Terminal 2)
\`\`\`bash
cd frontend-web
npm install && npm run dev
\`\`\`

3. **Desktop App** (Terminal 3)
\`\`\`bash
cd frontend-desktop
python -m venv venv && source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt && python main.py
\`\`\`

## Access Points

- **Web App:** http://localhost:5173
- **Backend:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

## Key Features

✓ User authentication and authorization
✓ CSV file upload and processing
✓ Real-time data analytics
✓ Interactive charts and visualizations
✓ Equipment data management
✓ PDF report generation
✓ Upload history tracking
✓ Responsive web and desktop UIs

## Architecture

\`\`\`
User Interface Layer
├── React Web Frontend (Chart.js, Recharts)
└── PyQt5 Desktop App (Matplotlib)

API Layer
└── Django REST Framework APIs

Data Layer
└── SQLite Database + Pandas Processing
\`\`\`

## Sample Data

A sample CSV file is included at \`data/sample_equipment_data.csv\` for testing.

Format:
\`\`\`
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-A-001,Centrifugal Pump,1200.5,45.2,65.8
\`\`\`

## Complete Setup Guide

For detailed step-by-step instructions, see [SETUP_GUIDE.md](./SETUP_GUIDE.md)

## File Structure

See [PROJECT_DOCUMENTATION.md](./PROJECT_DOCUMENTATION.md) for complete project structure and technical details.

## Technologies

- **Backend:** Django, Django REST Framework, Pandas, SQLite
- **Web:** React, Vite, Recharts, Tailwind CSS
- **Desktop:** PyQt5, Matplotlib
- **PDF:** ReportLab

## License

MIT License - See LICENSE file for details
\`\`\`
