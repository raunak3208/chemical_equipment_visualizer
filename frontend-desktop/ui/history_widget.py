from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from datetime import datetime

class HistoryWidget(QWidget):
    """Upload history widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Upload History (Last 5)')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # List
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        self.setLayout(layout)
    
    def update_history(self, history):
        """Update history list"""
        self.list_widget.clear()
        
        for batch in history:
            date_str = datetime.fromisoformat(batch['created_at'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
            
            item_text = (
                f"{batch['filename']} | {date_str}\n"
                f"Equipment: {batch['total_equipment']} | "
                f"Flowrate: {batch['avg_flowrate']:.2f} | "
                f"Pressure: {batch['avg_pressure']:.2f} | "
                f"Temperature: {batch['avg_temperature']:.2f}"
            )
            
            item = QListWidgetItem(item_text)
            self.list_widget.addItem(item)
