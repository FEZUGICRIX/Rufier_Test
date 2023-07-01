from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from instr import *

class Finalwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initui()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initui(self):
        self.txt_index = QLabel(txt_index)
        self.txt_workheart = QLabel(txt_workheart)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_index, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.txt_workheart, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)