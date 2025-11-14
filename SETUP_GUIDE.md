# Complete Setup Guide - Chemical Equipment Parameter Visualizer

This guide provides step-by-step instructions for setting up the entire hybrid application (Backend, Web Frontend, and Desktop Application).

## Project Structure

\`\`\`
chemical-equipment-visualizer/
├── backend/                         # Django Backend
│   ├── manage.py
│   ├── db.sqlite3                  # Database (auto-created)
│   ├── requirements.txt
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── equipment_api/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── migrations/
│   └── uploads/                    # CSV uploads directory
│
├── frontend-web/                    # React Web Frontend
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── services/
│   │   │   └── api.js
│   │   └── components/
│   │       ├── Login.jsx
│   │       ├── UploadForm.jsx
│   │       ├── DataTable.jsx
│   │       ├── Charts.jsx
│   │       ├── Summary.jsx
│   │       ├── History.jsx
│   │       └── [various CSS files]
│   └── node_modules/               # Dependencies (auto-installed)
│
├── frontend-desktop/                # PyQt5 Desktop Application
│   ├── main.py
│   ├── requirements.txt
│   ├── token.json                  # Auth token (auto-created)
│   ├── services/
│   │   └── api_client.py
│   └── ui/
│       ├── login_dialog.py
│       ├── main_window.py
│       ├── summary_widget.py
│       ├── charts_widget.py
│       ├── data_widget.py
│       └── history_widget.py
│
├── data/
│   └── sample_equipment_data.csv    # Sample CSV for testing
├── PROJECT_DOCUMENTATION.md         # Project overview
├── SETUP_GUIDE.md                  # This file
└── README.md                        # Quick start guide
\`\`\`

## Prerequisites

Before starting, ensure you have the following installed:

### For Backend
- Python 3.8 or higher
- pip (Python package manager)

### For Web Frontend
- Node.js 14 or higher
- npm or yarn

### For Desktop Application
- Python 3.8 or higher
- pip

### For All
- Git (optional, for version control)

## Step-by-Step Setup

### Phase 1: Backend Setup

#### 1.1 Navigate to Backend Directory

\`\`\`bash
cd backend
\`\`\`

#### 1.2 Create Virtual Environment

**On macOS/Linux:**
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

**On Windows:**
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

#### 1.3 Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### 1.4 Run Database Migrations

\`\`\`bash
python manage.py migrate
\`\`\`

#### 1.5 Create Superuser (Admin Account)

\`\`\`bash
python manage.py createsuperuser
\`\`\`

You'll be prompted to enter:
- Username: (e.g., admin)
- Email: (e.g., admin@example.com)
- Password: (enter a secure password)

#### 1.6 Start Backend Server

\`\`\`bash
python manage.py runserver
\`\`\`

Expected output:
\`\`\`
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
\`\`\`

**Backend is now running at:** \`http://localhost:8000\`

You can verify it's working by visiting: \`http://localhost:8000/admin/\` and logging in with your superuser credentials.

---

### Phase 2: Web Frontend Setup

#### 2.1 Navigate to Frontend Web Directory

Open a new terminal and navigate to the web frontend:

\`\`\`bash
cd frontend-web
\`\`\`

#### 2.2 Install Dependencies

\`\`\`bash
npm install
# or if you use yarn
yarn install
\`\`\`

#### 2.3 Start Development Server

\`\`\`bash
npm run dev
# or with yarn
yarn dev
\`\`\`

Expected output:
\`\`\`
VITE v4.3.0  ready in 234 ms

➜  Local:   http://localhost:5173/
➜  press h to show help
\`\`\`

**Web Frontend is now running at:** \`http://localhost:5173\`

---

### Phase 3: Desktop Application Setup

#### 3.1 Navigate to Desktop Application Directory

Open a new terminal and navigate to the desktop app:

\`\`\`bash
cd frontend-desktop
\`\`\`

#### 3.2 Create Virtual Environment

**On macOS/Linux:**
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

**On Windows:**
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`

#### 3.3 Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### 3.4 Run Desktop Application

\`\`\`bash
python main.py
\`\`\`

The PyQt5 application window will open with a login dialog.

---

## Testing the Application

### 1. Create User Accounts

You can create accounts through:

**Web Frontend:**
1. Go to \`http://localhost:5173\`
2. Click "No account? Register"
3. Enter username, email, and password
4. Click Register

**Desktop Application:**
1. Run the desktop app
2. Click the "Register" tab
3. Fill in the details
4. Click Register

**Backend Admin (for testing):**
1. Go to \`http://localhost:8000/admin/\`
2. You can create users directly from the admin panel

### 2. Upload Test Data

**Sample CSV file location:** \`data/sample_equipment_data.csv\`

**Via Web Frontend:**
1. Login with your credentials
2. Click "Upload CSV File"
3. Select \`data/sample_equipment_data.csv\`
4. Watch the data populate in tables and charts

**Via Desktop Application:**
1. Login with your credentials
2. Click "Upload CSV"
3. Select \`data/sample_equipment_data.csv\`
4. View data across Summary, Charts, and Data tabs

### 3. View Analytics

- Check summary statistics
- Examine equipment type distribution charts
- Review parameter trends and averages
- Download PDF reports

### 4. Upload History

Both applications track the last 5 uploads:
- View upload history with timestamps
- See statistics for each upload
- Track changes over time

---

## API Endpoints Reference

### Authentication

\`\`\`
POST /api/auth/login/
Body: {"username": "...", "password": "..."}
Response: {"token": "...", "user": {...}}

POST /api/auth/register/
Body: {"username": "...", "password": "...", "email": "..."}
Response: {"token": "...", "user": {...}}

POST /api/auth/logout/
Response: {"message": "Logged out successfully"}
\`\`\`

### Equipment Data

\`\`\`
POST /api/upload/
Headers: Authorization: Token {token}
Body: Form data with CSV file
Response: UploadBatch data

GET /api/summary/
Headers: Authorization: Token {token}
Response: Summary statistics

GET /api/data/
Headers: Authorization: Token {token}
Response: List of equipment

GET /api/history/
Headers: Authorization: Token {token}
Response: Last 5 uploads

GET /api/download-report/
Headers: Authorization: Token {token}
Response: PDF file
\`\`\`

---

## Troubleshooting

### Backend Issues

**Port 8000 already in use:**
\`\`\`bash
python manage.py runserver 8001
\`\`\`

**Database errors:**
\`\`\`bash
python manage.py migrate
\`\`\`

**Module not found errors:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Web Frontend Issues

**Port 5173 already in use:**
\`\`\`bash
npm run dev -- --port 5174
\`\`\`

**Module not found errors:**
\`\`\`bash
npm install
\`\`\`

**Cannot connect to backend:**
- Ensure backend is running on \`http://localhost:8000\`
- Check CORS settings in \`backend/config/settings.py\`

### Desktop Application Issues

**Connection refused:**
- Ensure backend is running
- Check API URL in \`services/api_client.py\`

**Library import errors:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**PyQt5 not displaying:**
- Ensure display server is available (on Linux, check DISPLAY variable)
- On some Linux systems, may need: \`pip install PyQt5 --config-settings --build-option="--qmake=/usr/bin/qmake"\`

---

## Important Notes

### Database

- SQLite database is stored in \`backend/db.sqlite3\`
- Only last 5 uploads are retained in history
- Deleting old uploads happens automatically

### Security

- Change \`SECRET_KEY\` in \`backend/config/settings.py\` for production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Update ALLOWED_HOSTS in settings.py for production domains

### CSV Format

The uploaded CSV must have exactly these columns:
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

Example:
\`\`\`
Equipment Name,Type,Flowrate,Pressure,Temperature
Pump-A-001,Centrifugal Pump,1200.5,45.2,65.8
\`\`\`

---

## Project Features

### Backend
- Django REST API with token authentication
- CSV file upload and processing with Pandas
- SQLite database for persistent storage
- PDF report generation with ReportLab
- CORS support for frontend connections
- Equipment type management and analytics

### Web Frontend
- React.js with responsive design
- Recharts for data visualization
- Real-time statistics dashboard
- Equipment data table view
- Upload history tracking
- PDF report download

### Desktop Application
- PyQt5 native UI
- Matplotlib charts
- Login/Register dialogs
- Data table display
- Chart visualization
- PDF report generation
- All same features as web app

---

## File Descriptions

### Backend Files

**config/settings.py**
- Django configuration
- CORS settings
- REST framework settings
- Database configuration

**equipment_api/models.py**
- UploadBatch model - metadata for uploads
- Equipment model - individual equipment records

**equipment_api/serializers.py**
- Data serialization for API responses
- Validation of input data

**equipment_api/views.py**
- API endpoints implementation
- CSV processing logic
- PDF generation
- Statistics calculation

### Web Frontend Files

**src/services/api.js**
- HTTP client for backend communication
- Authentication token management
- Request interceptors

**src/components/**
- Login.jsx - Authentication UI
- UploadForm.jsx - CSV file upload
- DataTable.jsx - Equipment data table
- Charts.jsx - Data visualization
- Summary.jsx - Statistics display
- History.jsx - Upload history

### Desktop Application Files

**services/api_client.py**
- HTTP client for API communication
- Token storage and management
- API method implementations

**ui/login_dialog.py**
- Login and registration dialog

**ui/main_window.py**
- Main application window
- Tab-based interface

**ui/*_widget.py**
- Individual UI components for each tab

---

## Next Steps After Setup

1. **Customize**: Modify styles and colors in CSS files
2. **Extend**: Add more equipment types or parameters
3. **Deploy**: Use Docker or cloud platforms for production
4. **Monitor**: Set up logging and monitoring
5. **Scale**: Implement caching and optimize queries

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Django documentation: https://docs.djangoproject.com
3. Review React documentation: https://react.dev
4. Review PyQt5 documentation: https://www.riverbankcomputing.com/static/Docs/PyQt5/
\`\`\`
