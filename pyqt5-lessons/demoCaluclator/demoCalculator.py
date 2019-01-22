# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 412)
        Dialog.setStyleSheet("background-color: rgb(239, 41, 41);")
        self.labelFirst = QtWidgets.QLabel(Dialog)
        self.labelFirst.setGeometry(QtCore.QRect(70, 70, 151, 21))
        self.labelFirst.setObjectName("labelFirst")
        self.labelSecond = QtWidgets.QLabel(Dialog)
        self.labelSecond.setGeometry(QtCore.QRect(70, 170, 151, 31))
        self.labelSecond.setObjectName("labelSecond")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(50, 330, 561, 61))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstNumber.setGeometry(QtCore.QRect(250, 70, 113, 25))
        self.lineEditFirstNumber.setObjectName("lineEditFirstNumber")
        self.lineEditSecondNumber = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondNumber.setGeometry(QtCore.QRect(280, 180, 113, 25))
        self.lineEditSecondNumber.setObjectName("lineEditSecondNumber")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(70, 280, 89, 25))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(230, 280, 89, 25))
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonDivide = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivide.setGeometry(QtCore.QRect(460, 280, 89, 25))
        self.pushButtonDivide.setObjectName("pushButtonDivide")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(350, 280, 89, 25))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.labelFirst.raise_()
        self.labelSecond.raise_()
        self.lineEditFirstNumber.raise_()
        self.lineEditSecondNumber.raise_()
        self.pushButtonPlus.raise_()
        self.pushButtonSubtract.raise_()
        self.pushButtonDivide.raise_()
        self.pushButtonMultiply.raise_()
        self.labelResult.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirst.setText(_translate("Dialog", "Enter First Number"))
        self.labelSecond.setText(_translate("Dialog", "Enter Second Number"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonDivide.setText(_translate("Dialog", "/"))
        self.pushButtonMultiply.setText(_translate("Dialog", "X"))

