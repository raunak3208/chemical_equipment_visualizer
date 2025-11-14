import sys
from PyQt5.QtWidgets import QApplication
from ui.login_dialog import LoginDialog
from ui.main_window import MainWindow
from services.api_client import APIClient

class EquipmentVisualizer:
    """Main application entry point"""
    
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.api = APIClient()
        self.show_login()
    
    def show_login(self):
        """Show login dialog"""
        login_dialog = LoginDialog()
        if login_dialog.exec_():
            self.api.user = login_dialog.user
            self.show_main_window()
        else:
            sys.exit(0)
    
    def show_main_window(self):
        """Show main application window"""
        self.main_window = MainWindow(self.api, self.api.user)
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = EquipmentVisualizer()
