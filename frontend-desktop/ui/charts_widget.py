from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class ChartsWidget(QWidget):
    """Charts visualization widget"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel('Charts & Visualizations')
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Chart containers
        self.figure = Figure(figsize=(12, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
    
    def update_charts(self, summary, data):
        """Update charts with data"""
        if not summary or not data:
            return
        
        self.figure.clear()
        
        # Type distribution
        ax1 = self.figure.add_subplot(131)
        types = summary.get('equipment_types', {})
        if types:
            ax1.pie(types.values(), labels=types.keys(), autopct='%1.1f%%')
            ax1.set_title('Equipment Type Distribution')
        
        # Average parameters
        ax2 = self.figure.add_subplot(132)
        params = ['Flowrate', 'Pressure', 'Temperature']
        values = [
            summary.get('avg_flowrate', 0),
            summary.get('avg_pressure', 0),
            summary.get('avg_temperature', 0)
        ]
        ax2.bar(params, values, color=['#1a56db', '#00a8e8', '#ffa502'])
        ax2.set_title('Average Parameters')
        ax2.set_ylabel('Value')
        
        # Parameter trends
        ax3 = self.figure.add_subplot(133)
        if len(data) > 0:
            equipment_names = [eq['equipment_name'][:10] for eq in data[:10]]
            flowrates = [eq['flowrate'] for eq in data[:10]]
            ax3.plot(equipment_names, flowrates, marker='o', color='#1a56db')
            ax3.set_title('Flowrate Trends')
            ax3.set_ylabel('Flowrate')
            plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)
        
        self.figure.tight_layout()
        self.canvas.draw()
