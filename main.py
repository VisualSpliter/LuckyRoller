import typing
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PySide6.QtGui import QGuiApplication, QIcon, QPalette, QColor, QFont
import sys

class qt_widget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setupUi()
        self.button.setText("Close")
        self.button.clicked.connect(self.close)

    def setupUi(self):
        msyh_font = QFont()
        msyh_font.setFamily(u"Microsoft YaHei UI")
        msyh_font.setPointSize(20)

        self.setWindowTitle("Hello")
        # self.resize(1920,1080)

        self.label = QLabel(self)
        self.label.setText("Welcome")
        self.label.setGeometry(80,50,150,20)

        self.button = QPushButton(self)
        self.button.setText("Close")
        self.button.setGeometry(120, 100, 200, 80)
        self.button.setFont(msyh_font)

if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    qt_window = qt_widget()
    qt_window.show()
    sys.exit(app.exec())

