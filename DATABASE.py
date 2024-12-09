import mysql.connector
from PyQt6.QtWidgets import QMessageBox


def connect_db(self):
    try:
        # MySQL database connection

        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hostel_mng"
        )
        return db
    except mysql.connector.Error as err:
        QMessageBox.critical(self, "Database Error", f"Error:{err}")
    except Exception as e:
        QMessageBox.critical(self, "Error", f"Error : {e}")