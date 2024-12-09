from mainwindow import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget





def switch_to_dashboardspage():
    test= Ui_MainWindow()
    test.stackedWidget.setCurrentIndex(0)