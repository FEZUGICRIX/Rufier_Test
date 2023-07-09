from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from instr import *

class Finalwindow(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initui()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)



    def result(self):
        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 100
        if int(self.exp.txt_age) >= 15:
            if self.index >= 15:
                return txt_res1

    def initui(self):
        self.work_test = QLabel(txt_workheart + str(self.result()))
        self.index_text = QLabel(txt_index + str(self.index))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.work_test, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
        print(self.index)