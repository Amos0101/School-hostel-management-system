from login_main import windowMain
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit


app = QApplication(sys.argv)

window = windowMain()
window.show()
app.exec()