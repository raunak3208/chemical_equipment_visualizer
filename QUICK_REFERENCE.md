# Quick Reference Guide

## Run Everything at Once

### macOS/Linux

\`\`\`bash
# Terminal 1 - Backend
cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver

# Terminal 2 - Web
cd frontend-web && npm install && npm run dev

# Terminal 3 - Desktop
cd frontend-desktop && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && python main.py
\`\`\`

### Windows

\`\`\`bash
# Terminal 1 - Backend
cd backend && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python manage.py migrate && python manage.py runserver

# Terminal 2 - Web
cd frontend-web && npm install && npm run dev

# Terminal 3 - Desktop
cd frontend-desktop && python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && python main.py
\`\`\`

## Common Tasks

### Create New Admin User
\`\`\`bash
cd backend
python manage.py createsuperuser
\`\`\`

### Reset Database
\`\`\`bash
cd backend
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
\`\`\`

### Change Backend Port
\`\`\`bash
python manage.py runserver 8001
\`\`\`

### Change Web Port
\`\`\`bash
npm run dev -- --port 5174
\`\`\`

## API Test URLs

### Login
\`\`\`
POST http://localhost:8000/api/auth/login/
{"username": "admin", "password": "password"}
\`\`\`

### Get Summary
\`\`\`
GET http://localhost:8000/api/summary/
Header: Authorization: Token YOUR_TOKEN
\`\`\`

## File Upload Format

Save as \`.csv\` with columns:
- Equipment Name
- Type
- Flowrate
- Pressure
- Temperature

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port already in use | Change port number |
| Module not found | Run pip install -r requirements.txt |
| Database locked | Delete db.sqlite3 and migrate again |
| Cannot connect to backend | Ensure backend is running on port 8000 |
| CORS errors | Check CORS settings in settings.py |

## Default Credentials

- **Admin User:** Created during setup
- **Test User:** Register via login page
\`\`\`
