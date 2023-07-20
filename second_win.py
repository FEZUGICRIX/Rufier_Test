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
        self.ob1 = False
        self.ob2 = False
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
        self.txt_age = QLineEdit()
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

    # Создание и настройки таймеров
    def timers(self, min, sec, start, settings_timers):
        self.timer = QTimer()
        self.time = QTime(0, min, sec)
        self.timer.timeout.connect(settings_timers)
        self.timer.start(start)

    def settings_timers(self, min, sec, style, style_for_timer3):
        self.timer = QTimer()
        self.time = QTime(0, min, sec)
        self.timer.timeout.connect(self.on_timer_timeout)
        self.timer.start(1000)

        self.timer_style = style
        self.timer_style_for_timer3 = style_for_timer3

    def on_timer_timeout(self):
        self.time = self.time.addSecs(-1)
        text = self.time.toString('hh:mm:ss')
        self.text_timer.setText(text)
        if self.timer_style_for_timer3:
            if self.time.toString("hh:mm:ss") > "00:00:45" or self.time.toString("hh:mm:ss") <= "00:00:15":
                self.text_timer.setStyleSheet(combined_style)
            elif self.time.toString("hh:mm:ss") <= "00:00:46" and self.time.toString("hh:mm:ss") >= "00:00:15":
                self.text_timer.setStyleSheet(style1)

        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    #Подключение методов таймера, при нажатии на соответствующую кнопку
    def connects_timers(self):
        self.txt_starttest1.clicked.connect(lambda: self.settings_timers(0, 16, None, False))
        self.txt_starttest2.clicked.connect(lambda: self.settings_timers(0, 31, QFont("Times", 36, QFont.Bold), False))
        self.txt_starttest3.clicked.connect(lambda: self.settings_timers(1, 1, combined_style, True))

    #Метод для создавания надписей в случае ошибки
    def input_error(self, text):
        if text == txt_error:
            if self.ob1:
                return
        else:
            if self.ob2:
                return
        self.input = QLabel(text)
        self.input.setStyleSheet(notification_styles)
        self.layout_time_v.addWidget(self.input, alignment=Qt.AlignVCenter)

    #Данный метод вызывается при нажатии на кнопку перехода на следуюший экран
    def connect(self):
        self.txt_sendresults.clicked.connect(self.check_input)

    # Метод проверки вводимых данных
    def check_input(self):
        age_text = self.txt_age.text()
        list_input = [self.txt_age, self.txt_hinttest1, self.txt_hinttest2, self.txt_hinttest3]
        error_fields = []

        for input_field in list_input:
            if input_field.text() == '' or not input_field.text().isdigit() or int(input_field.text()) < 0:
                error_fields.append(input_field)

        if len(error_fields) > 0:
            has_negative_number = any(not i.text().isdigit() for i in error_fields)
            if has_negative_number:
                self.input_error(txt_error)
                self.ob1 = True

            for field in error_fields:
                field.setStyleSheet("background-color: rgb(231, 183, 149); color: white;")
                field.setFont(QFont("Times", 10, QFont.Bold))
                field.setPlaceholderText('Error')

            has_negative_number = False
            error_fields.clear()
            self.connect()
            return

        if not age_text or int(age_text) < 7:
            self.input_error('Нельзя проводить тест, если вам меньше 7 лет!')
            self.ob2 = True

        else:
            self.next_click()

    # Переход на следующий экран, создание объекта класса Experiment
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.txt_hintname.text(),
                              self.txt_age.text(),
                              self.txt_hinttest1.text(),
                              self.txt_hinttest2.text(),
                              self.txt_hinttest3.text())
        self.tw = Finalwindow(self.exp)