import os
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QFileDialog
from about_window import AboutWindow

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""
        self.about_window = AboutWindow()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Grades Correction")
        self.setGeometry(100, 50, 560, 530)

        self.title = QLabel("Grades Correction", self)
        self.title.setObjectName("title")
        self.title.setGeometry(30, 20, 500, 40)

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(30, 80, 140, 35)
        self.load_button.clicked.connect(self.load_clicked)

        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(190, 80, 340, 35)

        self.bonus_label = QLabel("Bonus points:", self)
        self.bonus_label.setGeometry(30, 135, 140, 35)

        self.bonus_input = QLineEdit("0", self)
        self.bonus_input.setGeometry(190, 135, 100, 35)
        self.bonus_input.returnPressed.connect(self.bonus_entered)

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(30, 190, 500, 260)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.setColumnWidth(0, 140)
        self.table.setColumnWidth(1, 145)
        self.table.setColumnWidth(2, 145)
        self.table.setAlternatingRowColors(True)

        self.update_button = QPushButton("Update File", self)
        self.update_button.setGeometry(30, 470, 140, 35)
        self.update_button.clicked.connect(self.update_clicked)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(390, 470, 140, 35)
        self.about_button.clicked.connect(self.about_clicked)

    def load_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "Select grades file", "", "CSV files (*.csv)")[0]
        if file_name == "":
            return
        self.selected_file = file_name
        self.file_label.setText(os.path.basename(file_name))
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        with open(self.selected_file, "r") as f:
            next(f)
            for line in f:
                student_id, grade = line.strip().split(",")
                self.student_ids.append(student_id)
                self.original_grades.append(int(grade))
                self.corrected_grades.append(int(grade))
        self.update_table()

    def update_table(self):
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(self.student_ids[row]))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))
    
    def bonus_entered(self):
        bonus = int(self.bonus_input.text())
        for i in range(len(self.original_grades)):
            new_grade = self.original_grades[i] + bonus
            if new_grade > 100:
                new_grade = 100
            self.corrected_grades[i] = new_grade
        self.update_table()
   
    def update_clicked(self):
        if self.selected_file == "":
            return
        with open(self.selected_file, "w") as f:
            f.write("ID,Grade\n")
            for i in range(len(self.student_ids)):
                f.write(f"{self.student_ids[i]},{self.corrected_grades[i]}\n")
        self.open_file()

    def open_file(self):
        if sys.platform == "win32":
            os.startfile(self.selected_file)
        elif sys.platform == "darwin":
            subprocess.call(["open", self.selected_file])
        else:
            subprocess.call(["xdg-open", self.selected_file])

    def about_clicked(self):
        self.about_window.show()       

if __name__ == "__main__":
    app = QApplication()
    with open("style.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()
