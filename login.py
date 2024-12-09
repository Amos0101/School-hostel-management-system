# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 381)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.login_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.login_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.login_frame.setObjectName("login_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.login_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.login_frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.admin_lineEdit = QtWidgets.QLineEdit(parent=self.login_frame)
        self.admin_lineEdit.setMinimumSize(QtCore.QSize(0, 27))
        self.admin_lineEdit.setObjectName("admin_lineEdit")
        self.verticalLayout_2.addWidget(self.admin_lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.login_frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self.login_frame)
        self.password_lineEdit.setMinimumSize(QtCore.QSize(0, 27))
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.verticalLayout_3.addWidget(self.password_lineEdit)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sign_up_pushButton = QtWidgets.QPushButton(parent=self.login_frame)
        self.sign_up_pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.sign_up_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sign_up_pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.sign_up_pushButton.setCheckable(False)
        self.sign_up_pushButton.setAutoExclusive(False)
        self.sign_up_pushButton.setObjectName("sign_up_pushButton")
        self.verticalLayout.addWidget(self.sign_up_pushButton)
        self.cancel_pushButton = QtWidgets.QPushButton(parent=self.login_frame)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.cancel_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.cancel_pushButton.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.cancel_pushButton.setCheckable(False)
        self.cancel_pushButton.setAutoExclusive(False)
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.verticalLayout.addWidget(self.cancel_pushButton)
        self.register_pushButton = QtWidgets.QPushButton(parent=self.login_frame)
        self.register_pushButton.setMinimumSize(QtCore.QSize(0, 27))
        self.register_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.register_pushButton.setStyleSheet("color: rgb(0, 0, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.register_pushButton.setCheckable(False)
        self.register_pushButton.setAutoExclusive(False)
        self.register_pushButton.setObjectName("register_pushButton")
        self.verticalLayout.addWidget(self.register_pushButton)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.login_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Sign In"))
        self.label.setText(_translate("MainWindow", "Administrator ID"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.sign_up_pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.cancel_pushButton.setText(_translate("MainWindow", "Cancel"))
        self.register_pushButton.setText(_translate("MainWindow", "Register"))