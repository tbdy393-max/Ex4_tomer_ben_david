from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
import os


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.temperatures = []
        self.revenues = []
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

        self.draw_graph()

    def draw_graph(self):
        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)
        ax.plot([1, 2, 3, 4], [1, 4, 9, 16])
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication()
    with open("style.qss") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()