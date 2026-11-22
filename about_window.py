from PySide6.QtWidgets import QWidget, QLabel


class AboutWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("About")
        self.setGeometry(700, 150, 420, 200)

        self.name_label = QLabel("Tomer Ben-David", self)
        self.name_label.setObjectName("title")
        self.name_label.setGeometry(30, 20, 360, 40)

        self.info_label = QLabel("Grades correction app - Exercise 4", self)
        self.info_label.setGeometry(30, 75, 360, 30)

        self.link_label = QLabel('<a href="https://github.com/tbdy393-max/Ex4_tomer_ben_david">GitHub repository</a>', self)
        self.link_label.setGeometry(30, 120, 360, 30)
        self.link_label.setOpenExternalLinks(True)