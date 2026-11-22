import os
import sys
import subprocess
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QFileDialog


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Grades Correction")
        self.setGeometry(100, 100, 560, 640)

        self.title = QLabel("Grades Correction", self)
        self.title.setObjectName("title")
        self.title.setGeometry(30, 20, 500, 40)

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(30, 80, 140, 35)

        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(190, 80, 340, 35)

        self.bonus_label = QLabel("Bonus points:", self)
        self.bonus_label.setGeometry(30, 135, 140, 35)

        self.bonus_input = QLineEdit("0", self)
        self.bonus_input.setGeometry(190, 135, 100, 35)

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(30, 190, 500, 360)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.setColumnWidth(0, 140)
        self.table.setColumnWidth(1, 145)
        self.table.setColumnWidth(2, 145)

        self.update_button = QPushButton("Update File", self)
        self.update_button.setGeometry(30, 575, 140, 35)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(390, 575, 140, 35)


if __name__ == "__main__":
    app = QApplication()
    with open("style.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()
