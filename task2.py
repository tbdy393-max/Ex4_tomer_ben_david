from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from about_window import AboutWindow
import os
import numpy as np


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []
        self.about_window = AboutWindow()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Ice Cream Revenue")
        self.setGeometry(100, 50, 700, 530)

        self.title = QLabel("Ice Cream Revenue", self)
        self.title.setObjectName("title")
        self.title.setGeometry(30, 20, 640, 40)

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(30, 75, 140, 35)
        self.load_button.clicked.connect(self.load_clicked)

        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(190, 75, 480, 35)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.canvas.setParent(self)
        self.canvas.setGeometry(30, 160, 640, 300)

        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.toolbar.setGeometry(30, 120, 640, 35)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(530, 475, 140, 35)
        self.about_button.clicked.connect(self.about_clicked)

    def load_clicked(self):
        file_name = QFileDialog.getOpenFileName(self, "Select ice cream file", "", "CSV files (*.csv)")[0]
        if file_name == "":
            return
        self.file_label.setText(os.path.basename(file_name))
        self.temperatures = []
        self.revenues = []
        with open(file_name, "r") as f:
            next(f)
            for line in f:
                temperature, revenue = line.strip().split(",")
                self.temperatures.append(float(temperature))
                self.revenues.append(int(revenue))
        self.draw_graph()
       

    def draw_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.scatter(self.temperatures, self.revenues, s=1, label="Data")

        coefficients = np.polyfit(self.temperatures, self.revenues, 1)
        line_function = np.poly1d(coefficients)
        line_x = np.linspace(min(self.temperatures), max(self.temperatures), 100)
        line_y = line_function(line_x)
        ax.plot(line_x, line_y, color="red", label="Trend Line")
        ax.text(min(self.temperatures), max(self.revenues), f"y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}", color="red")

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Ice Cream Revenue vs. Temperature")
        ax.set_xlabel("Temperature [°C]")
        ax.set_ylabel("Revenue [$]")
        ax.legend()
        self.figure.tight_layout()
        self.canvas.draw()

    def about_clicked(self):
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication()
    with open("style.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()