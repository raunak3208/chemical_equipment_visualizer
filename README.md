Chemical Equipment Parameter Visualizer

Hybrid Application (Web + Desktop + Django API)

This project is a hybrid visualization system that includes:

Django REST API Backend

React Web Frontend

PyQt5 Desktop Application

CSV Upload & Analytics (Flowrate, Pressure, Temperature)

Charts (Chart.js & Matplotlib)

History of last 5 uploads

PDF Report Generation

📂 Project Structure
chemical_equipment/
│
├── backend/                # Django REST API
│   ├── equipment_api/
│   ├── config/
│   ├── uploads/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend-web/           # React Web App (Vite)
│   ├── src/
│   ├── index.html
│   ├── package.json
│
├── frontend-desktop/       # PyQt5 Desktop App
│   ├── main.py
│   ├── requirements.txt
│
└── README.md               # Documentation

🛠️ Requirements
Backend

Python 3.11

pip / venv

SQLite (default)

Frontend Web

Node 20 (recommended)

npm

Desktop

Python 3.11

PyQt5

⚙️ 1. Backend Setup (Django API)
📌 Step 1 — Navigate to Backend
cd backend

📌 Step 2 — Create Virtual Environment
python3.11 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows

📌 Step 3 — Install Dependencies
1) pip install --upgrade pip
   
2) pip install -r requirements.txt

📌 Step 4 — Run Migrations

1) python manage.py makemigrations
   
2) python manage.py migrate

🆕 STEP 5 — Initialize Database Using init_db (Admin Auto-Setup)

This project includes a custom Django management command that:

✔ Runs migrations
✔ Creates an admin user
✔ Sets up the uploads directory

Run:

python manage.py init_db


You should see:

[1/3] Running migrations...
✓ Migrations completed
[2/3] Creating admin user...
✓ Admin user created: admin
[3/3] Setting up directories...
✓ Uploads directory ready

============================================================
Database initialization completed successfully!
============================================================
Admin credentials:
  Username: admin
  Email: admin@example.com

Next: python manage.py runserver
============================================================

📌 Step 6 — Start Backend Server
python manage.py runserver


Backend is available at:

API Root → http://127.0.0.1:8000/api/

Admin Panel → http://127.0.0.1:8000/admin/

🌐 2. Frontend Web Setup (React + Vite)
📌 Step 1 — Navigate to Folder

-> cd frontend-web

📌 Step 2 — Install Dependencies

-> npm install

📌 Step 3 — Start Dev Server

-> npm run dev


Your web app runs here:

👉 http://localhost:5173/

🖥 3. Desktop App Setup (PyQt5 + Matplotlib)
📌 Step 1 — Navigate
cd frontend-desktop

📌 Step 2 — Create Virtual Environment
python3.11 -m venv venv
source venv/bin/activate

📌 Step 3 — Install Requirements
pip install -r requirements.txt

📌 Step 4 — Run App
python main.py

📊 Features
✔ CSV Upload

Supports columns:

Equipment Name

Type

Flowrate

Pressure

Temperature

✔ Summary Analytics

Backend computes:

Equipment count

Average flowrate, pressure, temperature

Type distribution

✔ Visualization

React → Chart.js

PyQt5 → Matplotlib

✔ Storage

Saves last 5 datasets

✔ PDF Reports

Auto-generated from backend
