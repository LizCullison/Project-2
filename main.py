import sys
from PyQt6.QtWidgets import QApplication
from calculator_gui import GUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())
