from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox, QTabWidget, QWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from services.api_client import APIClient

class LoginDialog(QDialog):
    """Login/Register dialog"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.api = APIClient()
        self.user = None
        self.setWindowTitle('Equipment Visualizer - Authentication')
        self.setGeometry(100, 100, 400, 300)
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Equipment Visualizer')
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Tab widget for Login/Register
        tabs = QTabWidget()
        tabs.addTab(self.create_login_tab(), 'Login')
        tabs.addTab(self.create_register_tab(), 'Register')
        layout.addWidget(tabs)
        
        self.setLayout(layout)
    
    def create_login_tab(self):
        """Create login tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Username:'))
        self.login_username = QLineEdit()
        layout.addWidget(self.login_username)
        
        layout.addWidget(QLabel('Password:'))
        self.login_password = QLineEdit()
        self.login_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.login_password)
        
        login_btn = QPushButton('Login')
        login_btn.clicked.connect(self.handle_login)
        layout.addWidget(login_btn)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_register_tab(self):
        """Create register tab"""
        widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Username:'))
        self.reg_username = QLineEdit()
        layout.addWidget(self.reg_username)
        
        layout.addWidget(QLabel('Email:'))
        self.reg_email = QLineEdit()
        layout.addWidget(self.reg_email)
        
        layout.addWidget(QLabel('Password:'))
        self.reg_password = QLineEdit()
        self.reg_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.reg_password)
        
        register_btn = QPushButton('Register')
        register_btn.clicked.connect(self.handle_register)
        layout.addWidget(register_btn)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def handle_login(self):
        """Handle login"""
        username = self.login_username.text()
        password = self.login_password.text()
        
        if not username or not password:
            QMessageBox.warning(self, 'Error', 'Please enter username and password')
            return
        
        success, result = self.api.login(username, password)
        if success:
            self.user = result
            self.accept()
        else:
            QMessageBox.critical(self, 'Login Failed', result)
    
    def handle_register(self):
        """Handle registration"""
        username = self.reg_username.text()
        email = self.reg_email.text()
        password = self.reg_password.text()
        
        if not username or not email or not password:
            QMessageBox.warning(self, 'Error', 'Please fill all fields')
            return
        
        success, result = self.api.register(username, password, email)
        if success:
            self.user = result
            self.accept()
        else:
            QMessageBox.critical(self, 'Registration Failed', result)
