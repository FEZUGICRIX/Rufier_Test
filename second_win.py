from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from final_win import Finalwindow

class Test_win(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.intui()
        self.connects_timers()
        self.connect()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def intui(self):
        # Создание виджетов
        self.txt_name = QLabel(txt_name)
        self.txt_hintname = QLineEdit(txt_hintname)
        self.txt_hintname.setPlaceholderText(txt_hintname)
        self.txt_age = QLabel(txt_age)
        self.txt_age1 = QLineEdit(txt_age)
        self.txt_age1.setPlaceholderText(txt_hintage)
        self.txt_test1 = QLabel(txt_test1)
        self.txt_starttest1 = QPushButton(txt_starttest1)
        self.txt_hinttest1 = QLineEdit(txt_hinttest1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_starttest2 = QPushButton(txt_starttest2)
        self.txt_test3 = QLabel(txt_test3)
        self.txt_starttest3 = QPushButton(txt_starttest3)
        self.txt_hinttest2 = QLineEdit(txt_hinttest2)
        self.txt_hinttest3 = QLineEdit(txt_hinttest3)
        self.txt_sendresults = QPushButton(txt_sendresults)
        self.text_timer = QLabel()
        # Создание лейаутов и размещение виджетов
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_name, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_hintname, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_age, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.txt_age1, alignment=Qt.AlignLeft)
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

    def connects_timers(self):
        self.txt_starttest1.clicked.connect(self.timer_test)
        self.txt_starttest2.clicked.connect(self.timer_sits)
        self.txt_starttest3.clicked.connect(self.timer_final)

    def connect(self):
        self.txt_sendresults.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.tw = Finalwindow()