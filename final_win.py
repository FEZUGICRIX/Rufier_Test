from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont
from instr import *

# 3 окно приложения
class Finalwindow(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.initui()
        self.show()

    #Метод настройки экрана
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet(style)

    def result(self):
        age = int(self.exp.txt_age)

        if age >= 15:
            self.calculation(15)
            return 15
        elif 13 <= age <= 14:
            self.calculation(16.5)
            return 16.5
        elif 11 <= age <= 12:
            self.calculation(18)
            return 18
        elif 9 <= age <= 10:
            self.calculation(19.5)
            return 19.5
        elif 7 <= age <= 8:
            self.calculation(21)
            return 21

    #Метод рассчета индекса руфье
    def calculation(self, start_index):
        self.index = (4 * (int(self.exp.test1) + int(self.exp.test2) + int(self.exp.test3)) - 200) / 100
        for i in range(5):
            if self.index >= start_index:
                return txt_res_list[i]
            else:
                if i == 1:
                    start_index -= 5
                    i += 1
                elif i == 2:
                    start_index -= 5.5
                    i += 1
                elif i == 3:
                    start_index -= 0.1
                    i += 1
                elif i == 4:
                    return txt_res_list[i]
                else:
                    start_index -= 4
                    i += 1

    # Метод создания и размещения виджетов
    def initui(self):
        # Создание виджетов
        label = QLabel()
        pixmap = QPixmap("image/img.png")
        label.setPixmap(pixmap)
        self.text = QLabel('Таблица, по которой был проведен рассчет⬇️⬇️⬇️')
        self.work_test = QLabel(self.exp.txt_hintname + " "  + txt_workheart + str(self.calculation(self.result())))
        self.index_text = QLabel(txt_index + str(self.index))
        # Создание лейаутов и размещение виджетов
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.work_test, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.layout.addWidget(label, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)