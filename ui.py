# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 335)
        Dialog.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(70, 180, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 210, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(0, 255, 255);")
        self.checkBox_2.setObjectName("checkBox_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 40, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"color: rgb(0, 0, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 0, 255);")
        self.label_2.setObjectName("label_2")
        self.btn_generete = QtWidgets.QPushButton(Dialog)
        self.btn_generete.setGeometry(QtCore.QRect(140, 260, 71, 21))
        self.btn_generete.setStyleSheet("color: rgb(255, 255, 127);\n"
"background-color: rgb(85, 0, 255);")
        self.btn_generete.setObjectName("btn_generete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBox.setText(_translate("Dialog", "Використовувати числа"))
        self.checkBox_2.setText(_translate("Dialog", "Використовувати алфавіт"))
        self.label.setText(_translate("Dialog", "Генератор паролів"))
        self.label_2.setText(_translate("Dialog", "Тут буде результат"))
        self.btn_generete.setText(_translate("Dialog", "Генератор"))

        def generat(self):
                print("click")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




class mainWindow():
        def __init__(self):
                super().__init__(self)
                self.window = Ui_MainWindow
                self.window.setupUi()
app = QApplication([])
main = mainWindow()
main.show
app.exac_()