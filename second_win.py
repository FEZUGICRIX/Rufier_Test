from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from final_win import Finalwindow

# 2 окно приложения
class Experiment():
    def __init__(self,txt_hintname, txt_age, test1, test2, test3):
        self.txt_hintname = txt_hintname
        self.txt_age = txt_age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class Test_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.intui()
        self.connects_timers()
        self.connect()
        self.checked = False
        self.show()

    #Метод настройки экрана
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        self.setStyleSheet(style)

    #Метод создания и размещения виджетов
    def intui(self):
        # Создание виджетов
        self.txt_name = QLabel(txt_name)
        self.txt_hintname = QLineEdit()
        self.txt_hintname.setPlaceholderText(txt_hintname)
        self.txt_age_label = QLabel(txt_age)
        self.txt_age = QLineEdit('0')
        self.txt_age.setPlaceholderText(txt_age)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit()
        self.txt_hinttest1.setPlaceholderText(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit()
        self.txt_hinttest2.setPlaceholderText(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit()
        self.txt_hinttest3.setPlaceholderText(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
        self.text_timer = QLabel()
        # Создание лейаутов и размещение виджетов
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_hintname, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_age_label, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_test1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_starttest1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_hinttest1, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_test2, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_starttest2, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_test3, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_starttest3, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_hinttest2, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_hinttest3, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_sendresults, alignment=Qt.AlignCenter)
        # Настройка лейаутов виджета таймер
        self.layout_time_v = QVBoxLayout()
        self.layout_time_h = QHBoxLayout()
        self.text_timer = QLabel(self)
        self.text_timer.setStyleSheet(style1)
        self.layout_time_v.addWidget(self.text_timer, alignment=Qt.AlignRight)
        self.layout_time_h.addLayout(self.layout)
        self.layout_time_h.addLayout(self.layout_time_v)
        self.setLayout(self.layout_time_h)

    #Метод для создавания надписей в случае ошибки
    def empty(self, text):
        self.empty_input = QLabel(text)
        self.empty_input.setStyleSheet('color:rgb(131, 49, 68)')
        self.empty_input.setFont(QFont('Georgia', 15, QFont.Bold))
        self.layout_time_v.addWidget(self.empty_input, alignment=Qt.AlignHCenter)

    #Создание 3 таймеров
    def timer_test(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 16)
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)  # Обновление каждую секунду

    def timer_sits(self):
        self.timer = QTimer()
        self.time = QTime(0, 0, 31)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)  # Обновление каждые 1,5 секунды

    def timer_final(self):
        self.timer = QTimer()
        self.time = QTime(0, 1, 1)
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    #Настройка 3 таймеров
    def timer1Event(self):
        self.time = self.time.addSecs(-1)
        text = self.time.toString('hh:mm:ss')
        self.text_timer.setText(text)
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        self.time = self.time.addSecs(-1)
        text = self.time.toString('hh:mm:ss')
        self.text_timer.setText(text)
        if self.time.toString("hh:mm:ss") > "00:00:45" or self.time.toString("hh:mm:ss") <= "00:00:15":
            self.text_timer.setStyleSheet(combined_style)
        elif self.time.toString("hh:mm:ss") <= "00:00:46" and  self.time.toString("hh:mm:ss") >= "00:00:15":
            self.text_timer.setStyleSheet(style1)
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer2Event(self):
        self.time = self.time.addSecs(-1)
        text = self.time.toString('hh:mm:ss'[6:8])
        self.text_timer.setText(text)
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    #Подключение методов таймера, при нажатии на соответствующую кнопку
    def connects_timers(self):
        self.txt_starttest1.clicked.connect(self.timer_test)
        self.txt_starttest2.clicked.connect(self.timer_sits)
        self.txt_starttest3.clicked.connect(self.timer_final)

    #Данный метод вызывается при нажатии на кнопку перехода на следуюший экран
    def connect(self):
        self.txt_sendresults.clicked.connect(self.check_input)

    #Метод проверки вводимых данных
    def check_input(self):
        age_text = self.txt_age.text()
        hint1_text = self.txt_hinttest1.text()
        hint2_text = self.txt_hinttest2.text()
        hint3_text = self.txt_hinttest3.text()

        list_input = [self.txt_age, self.txt_hinttest1, self.txt_hinttest2, self.txt_hinttest3]
        empty_fields = []

        for input_field in list_input:
            if input_field.text() == '':
                empty_fields.append(input_field)

        if len(empty_fields) > 0:
            if not self.checked:
                self.empty('Не все поля были заполнены!')
                self.checked = True
            for field in empty_fields:
                field.setStyleSheet("background-color: rgb(231, 183, 149); color: white;")
                field.setFont(QFont("Times", 10, QFont.Bold))
            if int(age_text) < 7:
                if not self.checked:
                    self.empty('Нельзя проводить тест, если вам меньше 7 лет!')
                    self.checked = True
        else:
            self.next_click()

    #Переход на следующий экран, создание объекта класса Experiment
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.txt_hintname.text(),
                              self.txt_age.text(),
                              self.txt_hinttest1.text(),
                              self.txt_hinttest2.text(),
                              self.txt_hinttest3.text())
        self.tw = Finalwindow(self.exp)