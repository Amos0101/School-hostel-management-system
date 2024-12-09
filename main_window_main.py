import sys
import mysql.connector
from PyQt6.QtCore import QDate
from reportlab.pdfgen import canvas

from mainwindow import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidget, QTableWidgetItem, \
    QHBoxLayout, QPushButton, QFileDialog
from DATABASE import connect_db


#from funcdash import dash
class main(Ui_MainWindow , QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("School management system")

        self.editing_student_id = None # track the student being edited

        self.dashboard.clicked.connect(self.switch_to_dashboardspage)

        self.student.clicked.connect(self.switch_to_studentspage)

        self.allocation.clicked.connect(self.switch_to_hostelpage)

        self.gender_comboBox.setPlaceholderText("Select gender")
        self.gender_comboBox.addItems(["Male","Female"])

        self.year_comboBox.setPlaceholderText("Select Year of Study")


        self.dob_dateEdit.setDate(QDate.currentDate())
        self.dor_dateEdit.setDate(QDate.currentDate())

        self.dob_dateEdit.setCalendarPopup(True)
        self.dor_dateEdit.setCalendarPopup(True)

        self.student_tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # Make table non-editable
        self.student_tableWidget.setColumnWidth(8, 150)  # Set width for the Action column

        self.set_schools_and_course = {
            "Computing and informatics":["IT",'COM','SIK','EDS'],
            "Education":["EDS",'ETS']

        }

        self.school_comboBox.setPlaceholderText("Select your school")
        self.course_comboBox.setPlaceholderText('Select your course')
        self.school_comboBox.addItems(self.set_schools_and_course.keys())
        self.school_comboBox.currentTextChanged.connect(self.update_course)

        self.load_student_table()
        self.register_pushButton.clicked.connect(self.save_student_data)

        self.pdf_pushButton.clicked.connect(self.export_to_pdf)

        self.go_to_student_reg_Button.clicked.connect(self.switch_to_studentspage)

    def update_course(self):
        school = self.school_comboBox.currentText()
        course = self.set_schools_and_course.get(school,[])

        self.course_comboBox.clear()
        self.course_comboBox.addItems(course)

    def switch_to_dashboardspage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_studentspage(self):
       self.stackedWidget.setCurrentIndex(1)

    def switch_to_hostelpage(self):
        self.stackedWidget.setCurrentIndex(2)

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

    def save_student_data(self):
        name = self.name_lineEdit.text().strip()
        reg_no = self.reg_no_lineEdit.text().strip()
        gender = self.gender_comboBox.currentText()
        dob = self.dob_dateEdit.date().toString("yyyy-MM-dd")
        school = self.school_comboBox.currentText()
        course = self.course_comboBox.currentText()
        dor = self.dor_dateEdit.date().toString("yyyy-MM-dd")
        year = self.year_comboBox.currentText()

        if not name or not reg_no or not gender or not dob or not school or not course or not dor or not year:
            QMessageBox.warning(self, "Validation Error", "Please fill in all the required fields.")
            return

        db = self.connect_db()
        cursor = db.cursor()
        query = """
                INSERT INTO students ( name,reg_no, gender, dob,school,course,dor,year)
                VALUES (%s, %s, %s, %s, %s, %s,%s,%s)
                """
        try:
            cursor.execute(query, (name,reg_no, gender, dob, school, course,dor,year))
            db.commit()

            QMessageBox.information(self, "Success", f"Student '{name}' has been registered successfully!")
            self.load_student_table()
            self.reset_form()
            self.dashboard()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error saving data: {e}")

    def load_student_table(self):
        db = self.connect_db()
        cursor = db.cursor()
        query = "SELECT * FROM students"

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            self.student_tableWidget.setRowCount(0)
            for row_data in results:
                row_position = self.student_tableWidget.rowCount()
                self.student_tableWidget.insertRow(row_position)
                for column, data in enumerate(row_data):
                    self.student_tableWidget.setItem(row_position, column, QTableWidgetItem(str(data)))

                    # Create buttons (Edit and Delete)
                    action_layout = QHBoxLayout()
                    edit_button = QPushButton("Edit")
                    edit_button.setStyleSheet("color: blue")


                    edit_button.clicked.connect(lambda _, row=row_data: self.populate_edit_form(row))
                    action_layout.addWidget(edit_button)

                    delete_button = QPushButton("Delete")
                    delete_button.setStyleSheet("color: red;")
                    delete_button.clicked.connect(lambda _, row=row_data[0]: self.delete_student(row))
                    action_layout.addWidget(delete_button)

                    #create a widget in the action column to hold buttond edit and delete
                    action_widget = QWidget()
                    action_widget.setLayout(action_layout)
                    self.student_tableWidget.setCellWidget(row_position, 8, action_widget)

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error loading data: {e}")

    def populate_edit_form(self, row_data):
        self.editing_student_id = row_data[0]
        self.name_lineEdit.setText(row_data[1])
        self.reg_no_lineEdit.setText(row_data[0])
        self.gender_comboBox.setCurrentText(row_data[2])
        self.dob_dateEdit.setDate(row_data[3])
        self.school_comboBox.setCurrentText(row_data[4])
        self.course_comboBox.setCurrentText(row_data[5])
        dor = self.dor_dateEdit.setDate(row_data[6])
        year = self.year_comboBox.setCurrentText(row_data[7])

        self.register_pushButton.setText("Save changes")
        self.register_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                               "font: 12pt \"MS Shell Dlg 2\";\n"
                                               "background-color: #3498db;")

        self.register_pushButton.clicked.disconnect()
        self.register_pushButton.clicked.connect(self.save_edited_student)

    def save_edited_student(self):
        if not self.editing_student_id:
            return

        name = self.name_lineEdit.text().strip()
        reg_no = self.reg_no_lineEdit.text().strip()
        gender = self.gender_comboBox.currentText()
        dob = self.dob_dateEdit.date().toString("yyyy-MM-dd")
        school = self.school_comboBox.currentText()
        course = self.course_comboBox.currentText()
        dor = self.dor_dateEdit.date().toString("yyyy-MM-dd")
        year = self.year_comboBox.currentText()

        db = self.connect_db()
        cursor = db.cursor()
        query = """
        UPDATE students
        SET reg_no = %s,name = %s, gender = %s, dob = %s, school= %s, course= %s, dor= %s, year= %s 
        WHERE reg_no = %s
        """
        try:
            cursor.execute(query, (name,reg_no, gender, dob,school, course,dor,year, self.editing_student_id))
            db.commit()
            QMessageBox.information(self, "Success", "Student details updated successfully.")
            self.load_student_table()
            self.reset_form()
            self.register_pushButton.setText("Register")
            self.register_pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "font: 12pt \"MS Shell Dlg 2\";\n"
                                                   "background-color: rgb(85, 255, 0);")
            self.register_pushButton.clicked.disconnect()
            self.register_pushButton.clicked.connect(self.save_student_data)

        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error updating data: {e}")

    def delete_student(self, reg_no):
        db = self.connect_db()
        cursor = db.cursor()
        query = "DELETE FROM students WHERE reg_no = %s"
        try:
            cursor.execute(query, (reg_no,))
            db.commit()

            QMessageBox.information(self, "Delete", f"Student with ID {reg_no} has been deleted.")
            self.load_student_table()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Database Error", f"Error deleting data: {e}")

    def reset_form(self):
        self.name_lineEdit.clear()
        self.reg_no_lineEdit.clear()
        self.gender_comboBox.setCurrentIndex(0)
        self.dob_dateEdit.setDate(QDate.currentDate())
        self.school_comboBox.setCurrentIndex(0)
        self.course_comboBox.setCurrentIndex(0)
        self.dor_dateEdit.setDate(QDate.currentDate())
        self.year_comboBox.setCurrentIndex(0)
        self.editing_student_id = None

    def export_to_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if not file_path:
            return
        pdf = canvas.Canvas(file_path)
        pdf.drawString(200, 800, "Student List")

        db = self.connect_db()
        cursor = db.cursor()
        query = "SELECT * FROM students"
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            y_position = 750
            for student in results:
                pdf.drawString(50, y_position, f"Name: {student[0]}, Reg no: {student[1]}, school:{student[4]},course: {student[5]},Reg Date:{student[6]},Year of study:{student[7]}")
                y_position -= 20
            pdf.save()
            QMessageBox.information(self, "Success", "Students' data exported to PDF successfully!")
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Error", f"Error exporting data to PDF: {e}")

    def dashboard(self):
        try:
            db = connect_db(self)
            cursor = db.cursor()

            # Fetch total students
            cursor.execute("SELECT COUNT(*) FROM students")
            total_students = cursor.fetchone()[0]

            # Update the labels with the data
            self.total_students_label.setText(f"Total Students: {total_students}")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error:{err}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error : {e}")



app = QApplication(sys.argv)
mainWindow = main()
mainWindow.show()
sys.exit(app.exec())