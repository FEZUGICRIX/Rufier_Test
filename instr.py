# Модуль с переменными
win_x, win_y = 400, 200
win_width, win_height = 1100, 600

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = (
    'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
    'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
    'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
    'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
    'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
    'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
    'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
    'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.\n'
    'Проба проводится у здоровых детей старше 7 лет. ')
txt_title = 'Проба Руфье'
txt_name = 'Введите Ф.И.О:'
txt_hintname = "Необязательно"
txt_age = 'Полных лет:'
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.'
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций.\n' \
            'Результаты запишите в соответствующие поля.'
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье:'
txt_workheart = 'Ваша работоспособность сердца: '

txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"
txt_res_list = [txt_res1, txt_res2, txt_res3, txt_res4, txt_res5]

txt_error = ('Ошибка! Возможная причина ошибки:\n'
                   '- Возможно, вы не заполнили какое-либо поле;\n'
                   '- Возможно, вы ввели отрицательное\вещественное число;\n'
                   '- Возможно, вы ввели текст.\n'
                   'Введите только цифры без доп. символов и попробуйте еще раз.')

# Стили
style1 = "font-size: 30px;"
style2 = "color:rgb(0,255,0)"
combined_style = style1 + style2

style = ('''
            background-color: rgb(237, 235, 220);
            font-family: Arial;
            font-size: 15px;
        }

        QPushButton {
            background-color: #d0c425;
            color: white;
            border: none;
            padding: 5px 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }

        QPushButton:hover {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                                        stop: 0 #45a049, stop: 1 #006400);
        }

        @keyframes pulse-animation {
            0% {
                transform: scale(1);
            }
            10% {
                transform: scale(1);
            }
            20% {
                transform: scale(1);
            }
            30% {
                transform: scale(1.2);
            }
            100% {
                transform: scale(1);
            }
        }

        QPushButton.animate {
            animation: pulse-animation 1s infinite;
        }

        QLineEdit {
            background-color: #f5f5f5;
            border: none;
            border-bottom: 2px solid #cccccc;
            padding: 5px;
            font-size: 16px;
            color: #333333;
        }

        QLineEdit:focus {
            background-color: #ffffff;
            border-bottom: 2px solid #3366ff;
            color: #000000;
        }

        QLineEdit::placeholder {
            color: #999999;
        }

        QLineEdit:hover {
            background-color: #f0f0f0;
        }

        QLineEdit:disabled {
            background-color: #dddddd;
            color: #888888;
        }

        QLabel {
            font-size: 17px;
            color: #333333;
        }

        QLabel:hover {
            color: #3366ff;
            text-decoration: underline;
        }

        QLabel:disabled {
            color: #888888;
}
        ''')

notification_styles = """
    QWidget {
        background-color: #f1c40f;
        border: 2px solid #e67e22;
        border-radius: 5px;
        padding: 10px;
    }

    QLabel::NoFrame {
        color: #ffffff;
        font-size: 12px;
    }
"""