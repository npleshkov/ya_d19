import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def input_gline(self, name, x, y):
        self.name_label = QLabel(self)
        self.name_label.setText(name)
        self.name_label.move(x, y)

        self.name_input = QLineEdit(self)
        self.name_input.move(x + 140, y)
        self.name_input.resize(40, 20)

    def main_qlcdnumber(self, variable, x, y):
        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(x, y)
        print(f'x {x}, y {y}')
        # self.LCD_count.display(variable)

    def main_calc(self):
        var1 = 20
        var2 = 30
        self.main_plus(var1, var2)
        # self.main_minus(var1, var2)
        # self.main_times(var1, var2)
        # self.main_dived(var1, var2)


    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Первая программа')

        self.btn = QPushButton('Расчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(150, 150)
        # self.btn.clicked.connect(self.hello)
        self.btn.clicked.connect(self.main_calc)

        # self.LCD_count = QLCDNumber(self)
        # self.LCD_count.move(110, 80)

        self.input_gline("Первый параметр: ", 10, 10)
        self.input_gline("Второй параметр: ", 10, 40)

    def hello(self):
        name = self.name_input.text()
        self.LCD_count.display(20)
        # self.label.setText("Привет, {}".format(name))

    def main_plus(self, var1, var2):
        plus = var1 + var2
        plus = 30
        print(f'var1 {var1}, var2 {var2}')
        self.main_qlcdnumber(plus, 150, 40)


    def main_minus(self, var1, var2):
        pass

    def main_times(self, var1, var2):
        pass

    def main_dived(self, var1, var2):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
