"""
A scientific calculator built with python and the PyQt5 gui library.
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from application_backend import update_display, Calc, set_display_text


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(10, 10, 421, 71))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setTextFormat(QtCore.Qt.PlainText)
        self.display.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.display.setWordWrap(False)
        self.display.setObjectName("display")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 410, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(120, 410, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(230, 410, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 330, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(120, 330, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(230, 330, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 250, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(120, 250, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(230, 250, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(120, 490, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.switch_sign = QtWidgets.QPushButton(self.centralwidget)
        self.switch_sign.setGeometry(QtCore.QRect(10, 490, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.switch_sign.setFont(font)
        self.switch_sign.setObjectName("switch_sign")
        self.period = QtWidgets.QPushButton(self.centralwidget)
        self.period.setGeometry(QtCore.QRect(230, 490, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.period.setFont(font)
        self.period.setObjectName("period")
        self.percentage = QtWidgets.QPushButton(self.centralwidget)
        self.percentage.setGeometry(QtCore.QRect(10, 170, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.percentage.setFont(font)
        self.percentage.setObjectName("percentage")
        self.btn_power_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_power_2.setGeometry(QtCore.QRect(120, 170, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_power_2.setFont(font)
        self.btn_power_2.setObjectName("btn_power_2")
        self.btn_sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sqrt.setGeometry(QtCore.QRect(230, 170, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(340, 170, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mul.setGeometry(QtCore.QRect(340, 250, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_mul.setFont(font)
        self.btn_mul.setObjectName("btn_mul")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(340, 330, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_sub.setFont(font)
        self.btn_sub.setObjectName("btn_sub")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(340, 410, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.btn_equ = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equ.setGeometry(QtCore.QRect(340, 490, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_equ.setFont(font)
        self.btn_equ.setObjectName("btn_equ")
        self.btn_sin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sin.setGeometry(QtCore.QRect(10, 100, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_sin.setFont(font)
        self.btn_sin.setObjectName("btn_sin")
        self.btn_cos = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cos.setGeometry(QtCore.QRect(120, 100, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_cos.setFont(font)
        self.btn_cos.setObjectName("btn_cos")
        self.btn_tan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tan.setGeometry(QtCore.QRect(230, 100, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_tan.setFont(font)
        self.btn_tan.setObjectName("btn_tan")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(340, 100, 93, 61))
        font = QtGui.QFont()
        font.setFamily("Victor Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adding the functions to the buttons
        for i in range(0, 10):
            exec(f'self.btn_{i}.clicked.connect(self.button_function_{i})')
        self.period.clicked.connect(self.period_button_function)
        self.btn_add.clicked.connect(self.add_button_function)
        self.btn_sub.clicked.connect(self.sub_button_function)
        self.btn_mul.clicked.connect(self.mul_button_function)
        self.btn_div.clicked.connect(self.div_button_function)
        self.btn_equ.clicked.connect(self.equ_button_function)

    def button_function_0(self):
        """Function for button click handling"""
        update_display(self.display, '0')

    def button_function_1(self):
        """Function for button click handling"""
        update_display(self.display, '1')

    def button_function_2(self):
        """Function for button click handling"""
        update_display(self.display, '2')

    def button_function_3(self):
        """Function for button click handling"""
        update_display(self.display, '3')

    def button_function_4(self):
        """Function for button click handling"""
        update_display(self.display, '4')

    def button_function_5(self):
        """Function for button click handling"""
        update_display(self.display, '5')

    def button_function_6(self):
        """Function for button click handling"""
        update_display(self.display, '6')

    def button_function_7(self):
        """Function for button click handling"""
        update_display(self.display, '7')

    def button_function_8(self):
        """Function for button click handling"""
        update_display(self.display, '8')

    def button_function_9(self):
        """Function for button click handling"""
        update_display(self.display, '9')

    def period_button_function(self):
        """Function to call when the user clicks the decimal point button"""
        nums = [str(i) for i in range(0, 10)]
        # Check if the . is in the text
        if '.' not in self.display.text():
            for num in nums:
                if self.display.text().endswith(num):
                    update_display(self.display, '.')
                    break

    def add_button_function(self):
        """Function to call when the add button is clicked"""
        invalid_chars = "+-/*."
        for char in invalid_chars:
            if self.display.text().endswith(char):
                return None
        update_display(self.display, '+')
    
    def sub_button_function(self):
        """Function to call when the add button is clicked"""
        invalid_chars = "+-/*."
        for char in invalid_chars:
            if self.display.text().endswith(char):
                return None
        update_display(self.display, '-')
    
    def mul_button_function(self):
        """Function to call when the add button is clicked"""
        invalid_chars = "+-/*."
        for char in invalid_chars:
            if self.display.text().endswith(char):
                return None
        update_display(self.display, '*')
    
    def div_button_function(self):
        """Function to call when the add button is clicked"""
        invalid_chars = "+-/*."
        for char in invalid_chars:
            if self.display.text().endswith(char):
                return None
        update_display(self.display, '/')
    
    def equ_button_function(self):
        set_display_text(self.display, str(Calc.evaluate(self.display.text())))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.display.setText(_translate("MainWindow", ""))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.switch_sign.setText(_translate("MainWindow", "+/-"))
        self.period.setText(_translate("MainWindow", "."))
        self.percentage.setText(_translate("MainWindow", "%"))
        self.btn_power_2.setText(_translate("MainWindow", "X^2"))
        self.btn_sqrt.setText(_translate("MainWindow", "X/(1/2)"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_mul.setText(_translate("MainWindow", "X"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_equ.setText(_translate("MainWindow", "="))
        self.btn_sin.setText(_translate("MainWindow", "sin(X)"))
        self.btn_cos.setText(_translate("MainWindow", "cos(X)"))
        self.btn_tan.setText(_translate("MainWindow", "tan(X)"))
        self.btn_clear.setText(_translate("MainWindow", "CE"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    with open('application_style.css', 'r') as StyleSheetFile:
        style = StyleSheetFile.read()
    app.setStyleSheet(style)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
