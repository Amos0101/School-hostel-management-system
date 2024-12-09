from PyQt6.QtWidgets import QMessageBox
import mysql.connector
from mainwindow import Ui_MainWindow
from DATABASE import connect_db
def dash(self):
    ui = Ui_MainWindow()
    try:
        db = connect_db(self)
        cursor = db.cursor()

        # Fetch total students
        cursor.execute("SELECT COUNT(*) FROM students")
        total_students = cursor.fetchone()[0]



        # Update the labels with the data
        ui.total_students_label.setText(f"Total Students: {total_students}")
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Database Error", f"Error:{err}")

    except Exception as e:
        QMessageBox.critical(self, "Error", f"Error : {e}")


