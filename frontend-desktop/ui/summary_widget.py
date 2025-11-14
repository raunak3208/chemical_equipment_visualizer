from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class SummaryWidget(QWidget):
    """Summary statistics widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Summary Statistics')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Stats grid
        stats_layout = QHBoxLayout()
        
        self.total_label = self.create_stat_box('Total Equipment', '0')
        stats_layout.addWidget(self.total_label)
        
        self.flowrate_label = self.create_stat_box('Avg Flowrate', '0.00')
        stats_layout.addWidget(self.flowrate_label)
        
        self.pressure_label = self.create_stat_box('Avg Pressure', '0.00')
        stats_layout.addWidget(self.pressure_label)
        
        self.temperature_label = self.create_stat_box('Avg Temperature', '0.00')
        stats_layout.addWidget(self.temperature_label)
        
        layout.addLayout(stats_layout)
        layout.addStretch()
        
        self.setLayout(layout)
    
    def create_stat_box(self, title, value):
        """Create a stat box"""
        group = QGroupBox(title)
        layout = QVBoxLayout()
        
        label = QLabel(value)
        label_font = QFont()
        label_font.setPointSize(24)
        label_font.setBold(True)
        label.setFont(label_font)
        label.setAlignment(Qt.AlignCenter)
        
        # Set color
        palette = label.palette()
        palette.setColor(label.foregroundRole(), QColor('#1a56db'))
        label.setPalette(palette)
        
        layout.addWidget(label)
        group.setLayout(layout)
        return group, label
    
    def update_summary(self, summary):
        """Update summary data"""
        _, label = self.total_label
        label.setText(str(summary.get('total_equipment', 0)))
        
        _, label = self.flowrate_label
        label.setText(f"{summary.get('avg_flowrate', 0):.2f}")
        
        _, label = self.pressure_label
        label.setText(f"{summary.get('avg_pressure', 0):.2f}")
        
        _, label = self.temperature_label
        label.setText(f"{summary.get('avg_temperature', 0):.2f}")
