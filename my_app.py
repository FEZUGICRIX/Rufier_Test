from second_win import*
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

# 1 окно приложения
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.intui()
        self.connect()
        self.show()

    #Метод настройки экрана
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet(style)

    #Метод создания и размещения виджетов
    def intui(self):
        #Создание виджетов
        self.txt_hello = QLabel(txt_hello)
        self.txt_instruction = QLabel(txt_instruction)
        self.link = QLabel()
        self.link.setText('<a href="https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%B1%D0%B0_%D0%A0%D1%83%D1%84%D1%8C%D0%B5_%E2%80%94_%D0%94%D0%B8%D0%BA%D1%81%D0%BE%D0%BD%D0%B0">Подробнее про тест руфье</a>')
        self.link.setOpenExternalLinks(True)
        self.link.setTextFormat(Qt.AutoText)
        self.txt_next = QPushButton(txt_next)
        #Размещение виджетов
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_hello, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.link, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.txt_next, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def connect(self):
        self.txt_next.clicked.connect(self.next_click)

    #Метод перехода на следующий экран
    def next_click(self):
        self.tw  = Test_win()
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    mw = MainWin()
    app.exec_()