import sys

from PyQt5 import uic, QtMultimedia, QtCore  # Импортируем uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QStatusBar
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from random import choice
from math import factorial
import sqlite3

mathematic = ['portret\portret.jpg', 'portret\portret2.jpg', 'portret\portret3.jpg', 'portret\portret4.jpg',
              'portret\portret5.jpg']  # Имена файлов с портретами математиков
evidence = ['facts\data.mp3', 'facts\data2.mp3', 'facts\data3.mp3', 'facts\data4.mp3',
            'facts\data5.mp3']  # Имена файлов с интересными фактами


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag_theme = True
        uic.loadUi('ui/untitled1.ui', self)  # Загружаем дизайн
        # Загружаем фоновую музыку
        self.load_mp3('test.mp3')
        # Устанавливаем громкость
        self.player.setVolume(5)
        # Запускается музыка
        self.player.play()
        self.btn_calc.clicked.connect(self.systemise)  # Подключаем кнопки меню к исполнительному методу
        self.tables.clicked.connect(self.systemise)
        self.plotting.clicked.connect(self.systemise)
        self.teoretic.clicked.connect(self.systemise)
        self.facts_btn.clicked.connect(self.facts)
        self.stopBtn.clicked.connect(self.player.stop)
        self.playBtn.clicked.connect(self.player.play)
        self.actionBlack_theme.triggered.connect(self.mode)
        self.actionStandart_theme.triggered.connect(self.mode)
        # В главном меню случайно выбирается фотография ученого
        self.pixmape = QPixmap(choice(mathematic))
        self.label_port.setPixmap(self.pixmape)

    def mode(self):
        if self.flag_theme:
            buttons = ['tables', 'teoretic', 'plotting', 'btn_calc', 'facts_btn', 'playBtn', 'stopBtn']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: rgb(200, 200, 200);")
            self.setStyleSheet('background-color: rgb(50, 50, 50);')
            self.label.setStyleSheet('color: rgb(200, 200, 200);')
            self.flag_theme = False
        else:
            buttons = ['tables', 'teoretic', 'plotting', 'btn_calc', 'facts_btn', 'playBtn', 'stopBtn']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.152,"
                                                     " y1:0.255682, x2:0.713, y2:0.443816, stop:0 rgba(120, 102, 202,"
                                                     " 255), stop:1 rgba(171, 242, 213, 255));")
            self.setStyleSheet('background-color: rgb(200, 200, 200);')
            self.label.setStyleSheet('color: rgb(0, 0, 0);')
            self.flag_theme = True

    def facts(self):
        # Метод случайно загружает интересный факт и воспроизводит его
        self.load_mp3(choice(evidence))
        self.player.setVolume(100)
        self.player.play()

    def load_mp3(self, filename):
        # Метод для воспроизведения музыки
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def systemise(self):
        # Метод для открытия дополнительных окон
        if self.sender().text() == 'Таблицы':
            self.tab1 = Tables()
            self.tab1.show()
        if self.sender().text() == 'Построение графиков':
            self.graf = Grafics()
            self.graf.show()
        if self.sender().text() == 'Теория':
            self.teor = Teoria()
            self.teor.show()
        if self.sender().text() == 'Калькулятор':
            self.w2 = Calculator()
            self.w2.show()


class Tables(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/tables.ui', self)  # Загружаем дизайн
        ## Изображение
        # Новое окно которое загружает изображения и выводит их на экран
        self.pixmap = QPixmap('image\таблица1.jpg')
        self.pixmap2 = QPixmap('image\таблица2.jpg')
        self.pixmap3 = QPixmap('image\таблица3.jpg')
        self.pixmap4 = QPixmap('image\таблица4.jpg')
        self.pixmap5 = QPixmap('image\таблица5.jpg')
        self.pixmap6 = QPixmap('image\таблица6.jpg')
        self.pixmap7 = QPixmap('image\таблица7.jpg')
        self.pixmap8 = QPixmap('image\таблица8.jpg')
        self.pixmap9 = QPixmap('image\таблица9.jpg')
        self.pixmap10 = QPixmap('image\таблица10.jpg')
        self.pixmap11 = QPixmap('image\таблица11.jpg')
        # Если картинки нет, то QPixmap будет пустым,
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)
        self.image2.setPixmap(self.pixmap2)
        self.image3.setPixmap(self.pixmap3)
        self.image4.setPixmap(self.pixmap4)
        self.image5.setPixmap(self.pixmap5)
        self.image6.setPixmap(self.pixmap6)
        self.image7.setPixmap(self.pixmap7)
        self.image8.setPixmap(self.pixmap8)
        self.image9.setPixmap(self.pixmap9)
        self.image10.setPixmap(self.pixmap10)
        self.image11.setPixmap(self.pixmap11)


class Teoria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag_theme = True
        uic.loadUi('ui/teoretic.ui', self)
        # Подключаем бызу данных в которой хранится теория за 7-9 класс
        self.con = sqlite3.connect('teoretic.db')
        cur = self.con.cursor()
        # В выпадающий список добавляются теория разделенная на признаки, свойства и теоремы
        self.cmbB_table.addItems(
            [jtem[0] for jtem in cur.execute("SELECT name FROM naimenovania").fetchall()])
        self.filter_btn.clicked.connect(self.filter)
        self.search_btn.clicked.connect(self.search)
        self.text_size.valueChanged.connect(self.size_txt)
        self.actionBlack_theme.triggered.connect(self.mode)
        self.actionStandart_theme.triggered.connect(self.mode)
        self.font = QtGui.QFont()

    def mode(self):
        if self.flag_theme:
            buttons = ['lineEdit', 'search_btn']
            buttons2 = ['cmbB_table', 'filter_btn', 'text_size']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: rgb(170, 170, 170);")
            for i in buttons2:
                eval('self.' + f'{i}').setStyleSheet("background-color: rgb(250, 250, 250);")
            self.setStyleSheet('background-color: rgb(50, 50, 50);')
            self.textEdit.setStyleSheet("background-color: rgb(200, 200, 200);")
            self.flag_theme = False
        else:
            buttons = ['lineEdit', 'search_btn']
            buttons2 = ['cmbB_table', 'filter_btn', 'text_size']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.152,"
                                                     " y1:0.255682, x2:0.713, y2:0.443816, stop:0 rgba(120, 102, 202,"
                                                     " 255), stop:1 rgba(171, 242, 213, 255));")
            for i in buttons2:
                eval('self.' + f'{i}').setStyleSheet('background-color: qlineargradient(spread:pad, x1:1,'
                                                     ' y1:1, x2:0.034, y2:0, stop:0 rgba(255, 255, 111, 255),'
                                                     ' stop:1 rgba(255, 255, 255, 255));')
            self.setStyleSheet('background-color: rgb(200, 200, 200);')
            self.flag_theme = True

    def size_txt(self):
        self.font.setPointSize(self.text_size.value())
        self.textEdit.setFont(self.font)

    def filter(self):
        # Метод выводит в listWidget всю теорию по данной теме
        self.textEdit.setText('')
        cur = self.con.cursor()
        result = cur.execute(
            f'''SELECT * FROM teoria WHERE what_is = {self.cmbB_table.currentIndex() + 1}''').fetchall()
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 1:
                    self.textEdit.append(f'{val}')
                    self.textEdit.append('')
        self.lineEdit.setText('')

    def search(self):
        # При вводе в строку поиск в listWidget выводится все найденные совпадения
        self.textEdit.setText('')
        cur = self.con.cursor()
        result = cur.execute(
            f"SELECT * FROM teoria WHERE title like '%{self.lineEdit.text()}%'").fetchall()
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                if j == 1:
                    self.textEdit.append(f'{val}')
                    self.textEdit.append('')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.search()


class Grafics(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag_theme = True
        uic.loadUi('ui/graph.ui', self)
        # В словарь добавляются основные графики
        self.EXCHANGE_RATES = {
            'Линейная функция': 'y = a * x + b',
            'Степенная функция': 'y = x ** a',
            'Обратно пропорциональная функция': 'y = a / x',
            'Квадратичная функция': 'y = a * x ** 2 + b * x + c'
        }
        # В выпадающий список добавляется словарь с ключами
        self.comboBox.addItems(self.EXCHANGE_RATES.keys())
        # И по изменению запускается функция
        self.comboBox.currentIndexChanged.connect(self.func)
        # Флаг нужен для того чтобы перерисовывать заново окно, позже мы это увидим
        self.flag = True
        self.work_btn.clicked.connect(self.work)
        self.dopBtn.clicked.connect(self.dopWork)
        # Вызывается функция
        self.func()
        # Рисуются компоненты для дополнительного окна
        self.statusBar = QStatusBar(self)
        self.statusBar.move(150, 150)
        self.statusBar.resize(259, 23)
        self.work_btn2 = QPushButton('Построить', self)
        self.work_btn2.move(290, 79)
        self.work_btn2.resize(159, 23)
        self.work_btn2.setStyleSheet(
            'background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.034, y2:0,'
            ' stop:0 rgba(255, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));')
        self.work_btn2.clicked.connect(self.work2)
        self.work_btn2.hide()
        self.dopLineEdit = QLineEdit(self)
        self.dopLineEdit.move(130, 79)
        self.dopLineEdit.resize(159, 23)
        self.dopLineEdit.setText('y = (x) ** -4')
        self.dopLineEdit.hide()
        self.help_btn = QPushButton('Помощь', self)
        self.help_btn.move(10, 79)
        self.help_btn.resize(118, 23)
        self.help_btn.setStyleSheet(
            'background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.034, y2:0,'
            ' stop:0 rgba(255, 255, 111, 255), stop:1 rgba(255, 255, 255, 255));')
        self.help_btn.clicked.connect(self.help)
        self.actionBlack_theme.triggered.connect(self.mode)
        self.actionStandart_theme.triggered.connect(self.mode)
        self.help_btn.hide()

    def mode(self):
        if self.flag_theme:
            buttons = ['comboBox', 'work_btn', 'dopBtn', 'help_btn', 'work_btn2', 'spinBox',
                       'spinBox_2', 'spinBox_3', 'dopLineEdit']
            buttons2 = ['label', 'label_2', 'label_3', 'label_4', 'label_5']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: rgb(200, 200, 200);")
            self.setStyleSheet('background-color: rgb(50, 50, 50);')
            for i in buttons2:
                eval('self.' + f'{i}').setStyleSheet("color: rgb(200, 200, 200);")
            self.flag_theme = False
        else:
            buttons = ['comboBox', 'work_btn', 'dopBtn', 'help_btn', 'work_btn2', 'spinBox',
                       'spinBox_2', 'spinBox_3']
            buttons2 = ['label', 'label_2', 'label_3', 'label_4', 'label_5']
            for i in buttons:
                eval('self.' + f'{i}').setStyleSheet("background-color: qlineargradient(spread:pad,"
                                                     " x1:1, y1:1, x2:0.034, y2:0, stop:0 rgba(255, 255,"
                                                     " 111, 255), stop:1 rgba(255, 255, 255, 255));")
            for i in buttons2:
                eval('self.' + f'{i}').setStyleSheet("color: rgb(0, 0, 0);")
            self.setStyleSheet('background-color: rgb(200, 200, 200);')
            self.flag_theme = True

    def func(self):
        # Метод выводит в label функцию, значение словаря и показывает поля для ввода коэфициэнта
        self.spinBox_3.hide()
        self.label_5.hide()
        self.spinBox_2.hide()
        self.label_4.hide()
        self.spinBox.hide()
        self.label_3.hide()
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.spinBox_3.setValue(0)
        self.label_2.setText(self.EXCHANGE_RATES[self.comboBox.currentText()])
        if self.comboBox.currentText() == 'Линейная функция':
            self.spinBox.show()
            self.label_3.show()
            self.spinBox_2.show()
            self.label_4.show()
        elif self.comboBox.currentText() == 'Степенная функция':
            self.spinBox.show()
            self.label_3.show()
        elif self.comboBox.currentText() == 'Обратно пропорциональная функция':
            self.spinBox.show()
            self.label_3.show()
        elif self.comboBox.currentText() == 'Квадратичная функция':
            self.spinBox_3.show()
            self.label_5.show()
            self.spinBox_2.show()
            self.label_4.show()
            self.spinBox.show()
            self.label_3.show()

    def dopWork(self):
        # Дополнительная функция скрывает основными методы для показа новых и отрисовки более сложных графиков
        if self.flag:
            self.spinBox_3.hide()
            self.label_5.hide()
            self.spinBox_2.hide()
            self.label_4.hide()
            self.spinBox.hide()
            self.label_3.hide()
            self.comboBox.hide()
            self.label_2.hide()
            self.work_btn.hide()
            self.dopBtn.setText('Вернуть обратно.')
            self.dopLineEdit.show()
            self.work_btn2.show()
            self.help_btn.show()
            self.flag = False
        else:
            # Скрывается дополнитнльные методы отрисовки и показываются основные
            self.comboBox.show()
            self.label_2.show()
            self.work_btn.show()
            self.dopLineEdit.hide()
            self.work_btn2.hide()
            self.help_btn.hide()
            self.statusBar.showMessage('')
            self.dopBtn.setText('Более сложные графики')
            self.flag = True
            self.func()

    def work2(self):
        # Функция для отрисовки усложненных графиков
        try:
            if self.dopLineEdit.text().find('y = ') < self.dopLineEdit.text().find(
                'x') and self.dopLineEdit.text().find('y =') != -1 and self.dopLineEdit.text().find(
                '(') < self.dopLineEdit.text().find('x') and self.dopLineEdit.text().find(
                ')') > self.dopLineEdit.text().find('x') and self.dopLineEdit.text().find(
                '(') != -1 and self.dopLineEdit.text().find(')') != -1:
                self.statusBar.showMessage('')
                self.GraphWidget.clear()
                if '** 0.' in self.dopLineEdit.text() or '** (' in self.dopLineEdit.text():
                    a = []
                    b = []
                    for i in range(0, 11):
                        try:
                            a.append(eval(self.dopLineEdit.text().replace('x', f'{i}')[4:]))
                            b.append(i)
                        except ZeroDivisionError:
                            continue
                    self.GraphWidget.plot(b, a)
                else:
                    a = []
                    b = []
                    for i in range(-10, 1):
                        try:
                            a.append(eval(self.dopLineEdit.text().replace('x', f'{i}')[4:]))
                            b.append(i)
                        except ZeroDivisionError:
                            continue
                    self.GraphWidget.plot(b, a)
                    a = []
                    b = []
                    for i in range(0, 11):
                        try:
                            a.append(eval(self.dopLineEdit.text().replace('x', f'{i}')[4:]))
                            b.append(i)
                        except ZeroDivisionError:
                            continue
                    self.GraphWidget.plot(b, a)
            else:
                self.statusBar.showMessage(f'Неправильный формат ввода функции!')
        except NameError:
            pass

    def help(self):
        self.help = Help_Window()
        self.help.show()

    def work(self):
        # Основной метод для отрисовки графика
        self.GraphWidget.clear()
        # Проверяется по ключу какой график надо строить
        if self.comboBox.currentText() == 'Линейная функция':
            self.GraphWidget.plot([i for i in range(-10, 11)],
                                  [self.spinBox.value() * i + self.spinBox_2.value() for i in range(-10, 11)])
        elif self.comboBox.currentText() == 'Степенная функция' and self.spinBox.value() < 0:
            self.GraphWidget.plot([i for i in range(-10, 1) if i != 0],
                                  [i ** self.spinBox.value() for i in range(-10, 1) if i != 0])
            self.GraphWidget.plot([i for i in range(1, 11) if i != 0],
                                  [i ** self.spinBox.value() for i in range(1, 11) if i != 0])
        elif self.comboBox.currentText() == 'Степенная функция':
            self.GraphWidget.plot([i for i in range(-10, 11)],
                                  [i ** self.spinBox.value() for i in range(-10, 11)])
        elif self.comboBox.currentText() == 'Обратно пропорциональная функция':
            self.GraphWidget.plot([i for i in range(-10, 1) if i != 0],
                                  [self.spinBox.value() / i for i in range(-10, 1) if i != 0])
            self.GraphWidget.plot([i for i in range(1, 11) if i != 0],
                                  [self.spinBox.value() / i for i in range(1, 11) if i != 0])
        elif self.comboBox.currentText() == 'Квадратичная функция':
            self.GraphWidget.plot([i for i in range(-10, 11)],
                                  [self.spinBox.value() * i ** 2 + self.spinBox_2.value() * i + self.spinBox_3.value()
                                   for i in range(-10, 11)])


class Help_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/help.ui', self)


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/calc.ui', self)  # Загружаем дизайн
        # Последний класс для калькулятора
        self.flag = 0
        self.display_type = '0'
        self.name = ''
        # Дополнительные флаги для проверки
        self.counter = 0
        self.counter1 = 0
        self.minus = 0
        self.nul = 0
        self.tochka = 0
        btn = 0
        # Подключение 10 кнопок от 9 - 0
        for i in range(9):
            eval('self.btn' + str(btn)).clicked.connect(self.set_of_numbers)
            btn += 1
        # Подключение других кнопок не связанные с числами
        self.btn_div.clicked.connect(self.button)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_dot.clicked.connect(self.set_of_numbers)
        self.btn_eq.clicked.connect(self.ravno)
        self.btn_fact.clicked.connect(self.button)
        self.btn_minus.clicked.connect(self.button)
        self.btn_mult.clicked.connect(self.button)
        self.btn_plus.clicked.connect(self.button)
        self.btn_pow.clicked.connect(self.button)
        self.btn_sqrt.clicked.connect(self.button)

    def clear(self):
        # Метод для очистки калькулятора
        self.table.display(0)
        self.flag = 0
        self.counter = 0
        self.counter1 = 0
        self.minus = 0
        self.nul = 0
        self.tochka = 0
        self.display_type = '0'
        self.display_type2 = '0'
        self.name = ''

    def set_of_numbers(self):
        # Метод для проверки веденного числа и его запоминания в переменную
        if self.flag == 0:
            if self.sender().text() == '0':
                self.display_type = ''
            else:
                if self.tochka == 0 and self.sender().text() == '.' and self.display_type.find('.') == -1:
                    self.display_type = '0.'
                    self.table.display(self.display_type)
                    self.tochka = 1
                    self.flag = 1
                else:
                    self.display_type = ''
                    self.flag = 1
                    self.display_type = f'{self.display_type}' + f'{self.sender().text()}'
                    self.table.display(f'{self.display_type}')
        elif self.flag == 1:
            if self.display_type.find('.') == -1:
                self.display_type = f'{self.display_type}' + f'{self.sender().text()}'
                self.table.display(f'{self.display_type}')
                self.tochka = 0
            else:
                if self.sender().text() != '.':
                    self.display_type = f'{self.display_type}' + f'{self.sender().text()}'
                    self.table.display(f'{self.display_type}')

    def button(self):
        # Метод который проверяет арифмитические методы
        self.display_type2 = self.display_type
        if self.sender().text() == '+':
            self.name = f'{self.display_type2}+'
            self.display_type = ''
        elif self.sender().text() == '-':
            if self.display_type == '0':
                self.display_type = '-'
                self.flag = 1
            elif self.name != '':
                self.display_type = '-'
                self.flag = 1
            else:
                self.name = f'{self.display_type2}-'
                self.display_type = ''
        elif self.sender().text() == '*':
            self.name = f'{self.display_type2}*'
            self.display_type = ''
        elif self.sender().text() == '/':
            self.name = f'{self.display_type2}/'
            self.display_type = '0'
        elif self.sender().text() == '^':
            self.name = f'{self.display_type2}**'
            self.display_type = ''
        elif self.sender().text() == '√':
            self.name = f'{self.display_type2}**0.5'
            self.counter = 1
            self.display_type = ''
            self.ravno()
        elif self.sender().text() == '!':
            self.name = f'{self.display_type2}'
            self.counter1 = 1
            self.display_type = ''
            self.ravno()

    def ravno(self):
        # Метод который считает два числа
        try:
            if self.counter == 0 and self.counter1 == 0 and self.name[-1] == '/' and self.display_type == '0':
                self.table.display('Error')
            elif self.counter == 0 and self.counter1 == 0:
                self.table.display(eval(self.name + self.display_type))
                self.display_type = eval(self.name + self.display_type)
                self.display_type2 = self.display_type
            elif self.counter == 1 and self.name[0] == '-':
                self.table.display('Error')
            elif self.counter == 1:
                self.table.display(eval(self.name))
                self.counter = 0
                self.display_type = eval(self.name)
                self.display_type2 = self.display_type
            elif self.counter1 == 1 and self.name == '' and self.name == 0:
                self.table.display('1')
                self.display_type2 = self.display_type
            elif self.counter1 == 1:
                self.name = int(float(self.name))
                self.table.display(f"{factorial(int(self.name))}")
                self.counter1 = 0
                self.display_type = f"{factorial(int(self.name))}"
        except TypeError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
