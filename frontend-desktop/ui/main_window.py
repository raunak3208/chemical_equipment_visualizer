from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QFileDialog, QMessageBox, QTabWidget, QScrollArea
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from services.api_client import APIClient
from ui.data_widget import DataWidget
from ui.charts_widget import ChartsWidget
from ui.history_widget import HistoryWidget
from ui.summary_widget import SummaryWidget
import os

class UploadThread(QThread):
    """Thread for uploading CSV file"""
    finished = pyqtSignal(bool, str)
    
    def __init__(self, api, file_path):
        super().__init__()
        self.api = api
        self.file_path = file_path
    
    def run(self):
        success, result = self.api.upload_csv(self.file_path)
        msg = f"Uploaded {result.get('total_equipment', 0)} equipment records" if success else str(result)
        self.finished.emit(success, msg)

class MainWindow(QMainWindow):
    """Main application window"""
    
    def __init__(self, api, user):
        super().__init__()
        self.api = api
        self.user = user
        self.data = []
        self.summary = None
        self.history = []
        
        self.setWindowTitle('Chemical Equipment Parameter Visualizer')
        self.setGeometry(100, 100, 1400, 900)
        self.init_ui()
        self.load_data()
    
    def init_ui(self):
        """Initialize UI"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        
        # Header
        header = QHBoxLayout()
        title = QLabel('Chemical Equipment Parameter Visualizer')
        title_font = QFont()
        title_font.setPointSize(14)
        title_font.setBold(True)
        title.setFont(title_font)
        header.addWidget(title)
        
        header.addStretch()
        
        user_label = QLabel(f'User: {self.user["username"]}')
        header.addWidget(user_label)
        
        upload_btn = QPushButton('Upload CSV')
        upload_btn.clicked.connect(self.handle_upload)
        header.addWidget(upload_btn)
        
        download_btn = QPushButton('Download Report')
        download_btn.clicked.connect(self.handle_download_report)
        header.addWidget(download_btn)
        
        logout_btn = QPushButton('Logout')
        logout_btn.clicked.connect(self.handle_logout)
        header.addWidget(logout_btn)
        
        layout.addLayout(header)
        
        # Tabs
        tabs = QTabWidget()
        
        # Summary tab
        self.summary_widget = SummaryWidget()
        tabs.addTab(self.summary_widget, 'Summary')
        
        # Charts tab
        self.charts_widget = ChartsWidget()
        tabs.addTab(self.charts_widget, 'Charts')
        
        # Data tab
        self.data_widget = DataWidget()
        tabs.addTab(self.data_widget, 'Data')
        
        # History tab
        self.history_widget = HistoryWidget()
        tabs.addTab(self.history_widget, 'History')
        
        layout.addWidget(tabs)
        
        central_widget.setLayout(layout)
    
    def handle_upload(self):
        """Handle CSV upload"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Select CSV File', '', 'CSV Files (*.csv)'
        )
        
        if not file_path:
            return
        
        self.upload_thread = UploadThread(self.api, file_path)
        self.upload_thread.finished.connect(self.on_upload_finished)
        self.upload_thread.start()
    
    def on_upload_finished(self, success, message):
        """Handle upload completion"""
        if success:
            QMessageBox.information(self, 'Success', message)
            self.load_data()
        else:
            QMessageBox.critical(self, 'Error', message)
    
    def load_data(self):
        """Load data from backend"""
        success, summary = self.api.get_summary()
        if success:
            self.summary = summary
            self.summary_widget.update_summary(summary)
        
        success, data = self.api.get_data()
        if success:
            self.data = data
            self.data_widget.update_data(data)
            self.charts_widget.update_charts(self.summary, data)
        
        success, history = self.api.get_history()
        if success:
            self.history = history
            self.history_widget.update_history(history)
    
    def handle_download_report(self):
        """Handle PDF report download"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, 'Save Report', 'equipment_report.pdf', 'PDF Files (*.pdf)'
        )
        
        if not file_path:
            return
        
        success, message = self.api.download_report(file_path)
        if success:
            QMessageBox.information(self, 'Success', 'Report downloaded successfully')
            os.startfile(file_path) if os.name == 'nt' else os.system(f'open {file_path}')
        else:
            QMessageBox.critical(self, 'Error', message)
    
    def handle_logout(self):
        """Handle logout"""
        self.api.logout()
        self.close()
