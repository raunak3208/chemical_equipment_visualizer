from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QScrollArea
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class DataWidget(QWidget):
    """Equipment data table widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Equipment Data')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            'Equipment Name', 'Type', 'Flowrate', 'Pressure', 'Temperature'
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
        
        self.setLayout(layout)
    
    def update_data(self, data):
        """Update table with equipment data"""
        self.table.setRowCount(len(data))
        
        for row, equipment in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(equipment['equipment_name']))
            self.table.setItem(row, 1, QTableWidgetItem(equipment['equipment_type']))
            self.table.setItem(row, 2, QTableWidgetItem(f"{equipment['flowrate']:.2f}"))
            self.table.setItem(row, 3, QTableWidgetItem(f"{equipment['pressure']:.2f}"))
            self.table.setItem(row, 4, QTableWidgetItem(f"{equipment['temperature']:.2f}"))
