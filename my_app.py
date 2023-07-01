from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from instr import *
from second_win import Test_win
from final_win import Finalwindow
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.intui()
        self.connect()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def intui(self):
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.txt_next = QPushButton(txt_next)
        self.txt_instruction = QLabel(txt_instruction)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_hello, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)
    def connect(self):
        self.txt_next.clicked.connect(self.next_click)
    def next_click(self):
        self.tw  = Test_win()
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    mw = MainWin()
    app.exec_()