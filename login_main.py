import sys

from PyQt6.QtCore import Qt, QDate
import mysql.connector
from login import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLineEdit
from register import Ui_Form
from DATABASE import connect_db
from dashboard import dash
class windowMain(Ui_MainWindow , QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("School management system")
        self.centralwidget.layout().setAlignment(self.login_frame, Qt.AlignmentFlag.AlignCenter)

        self.register_pushButton.clicked.connect(self.show_register)

        self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.sign_up_pushButton.clicked.connect(self.handle_login)
        self.cancel_pushButton.clicked.connect(self.reset_login_form)

    def handle_login(self):
        id = self.admin_lineEdit.text()
        passwd = self.password_lineEdit.text()
        try:
            db = connect_db(self)
            cursor = db.cursor()
            if id and passwd:
                db = connect_db(self)
                cursor = db.cursor()

                cursor.execute("SELECT * FROM register WHERE id = %s and password = %s", (id, passwd))
                result = cursor.fetchone()

                if result:

                    self.open_main_window()
                    QMessageBox.information(self, "Login", f"Logged in successfully!")
                else:
                    QMessageBox.warning(self,"Login",f"Invalid Id or password")
                    self.reset_login_form()
            else:
                QMessageBox.warning(self, "Validation Error", "Please fill in all the required fields.")

            cursor.close()
            db.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error:{err}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error : {e}")


    def show_register(self):
        self.centralwidget.layout().removeWidget(self.login_frame)
        self.login_frame.hide()

        self.register_form = QWidget(self)
        self.register_ui = Ui_Form()
        self.register_form.setFixedSize(360, 450)
        self.register_ui.setupUi(self.register_form)

        self.register_ui.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_ui.con_password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_ui.dateEdit.setCalendarPopup(True)

        self.centralwidget.layout().addWidget(self.register_form)
        self.centralwidget.layout().setAlignment(self.register_form, Qt.AlignmentFlag.AlignCenter)
        self.register_ui.back_pushButton.clicked.connect(self.return_to_login)
        self.register_ui.sign_in_pushButton.clicked.connect(self.handle_register)
        self.register_ui.cancel_pushButton.clicked.connect(self.reset_register_form)
    def handle_register(self):
        #register_ui = Ui_Form()
        name = self.register_ui.name_lineEdit.text()
        id = self.register_ui.adminID_lineEdit.text()
        phone =self.register_ui.phone_lineEdit.text()
        passwd = self.register_ui.password_lineEdit.text()
        conpasswd = self.register_ui.con_password_lineEdit.text()
        date = self.register_ui.dateEdit.date().toString("yyyy-MM-dd")

        if name and id and passwd and conpasswd and phone and date:
            if passwd == conpasswd:
                try:
                    conn = connect_db(self)
                    cursor = conn.cursor()

                    cursor.execute("INSERT INTO register(name,id,phone,password,dor)"
                                   "values(%s,%s,%s,%s,%s)",(name,id,phone,passwd,date))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    QMessageBox.information(self, "Success", f"Admin '{name}' has been registered successfully!")
                    self.reset_register_form()
                    self.return_to_login()
                except mysql.connector.Error as err:
                    QMessageBox.critical(self, "Database Error", f"Error:{err}")
                    print(f"Database error : {err}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error : {e}")
                    print(f"Error : {e}")

            else:
                QMessageBox.critical(self, "Error", f"Password Mismatch")
                self.register_ui.password_lineEdit.clear()
                self.register_ui.con_password_lineEdit.clear()

        else:
            QMessageBox.warning(self, "Validation Error", "Please fill in all the required fields.")
    def reset_register_form(self):
        self.register_ui.name_lineEdit.clear()
        self.register_ui.adminID_lineEdit.clear()
        self.register_ui.phone_lineEdit.clear()
        self.register_ui.password_lineEdit.clear()
        self.register_ui.con_password_lineEdit.clear()
        self.register_ui.dateEdit.setDate(QDate.currentDate())

    def reset_login_form(self):
        self.admin_lineEdit.clear()
        self.password_lineEdit.clear()
    def return_to_login(self):
        #clear the register form and show login
        self.centralwidget.layout().removeWidget(self.register_form)
        self.register_form.deleteLater()
        self.login_frame.show()

        self.centralwidget.layout().setAlignment(self.login_frame, Qt.AlignmentFlag.AlignCenter)

    def open_main_window(self):
        from main_window_main import main
        self.windo = main()
        self.windo.show()
        self.hide()

'''app = QApplication(sys.argv)
window = windowMain()
window.show()
app.exec()'''