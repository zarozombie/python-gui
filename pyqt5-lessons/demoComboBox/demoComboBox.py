# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(675, 632)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 190, 20))
        self.label.setObjectName("label")
        self.labelAcountBox = QtWidgets.QLabel(Dialog)
        self.labelAcountBox.setGeometry(QtCore.QRect(110, 230, 420, 110))
        self.labelAcountBox.setText("")
        self.labelAcountBox.setObjectName("labelAcountBox")
        self.comboBoxAccountType = QtWidgets.QComboBox(Dialog)
        self.comboBoxAccountType.setGeometry(QtCore.QRect(260, 120, 340, 25))
        self.comboBoxAccountType.setObjectName("comboBoxAccountType")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select your Account type"))
        self.comboBoxAccountType.setItemText(0, _translate("Dialog", "Savings Account"))
        self.comboBoxAccountType.setItemText(1, _translate("Dialog", "Current Account"))
        self.comboBoxAccountType.setItemText(2, _translate("Dialog", "Recurring Account"))
        self.comboBoxAccountType.setItemText(3, _translate("Dialog", "Fixed Deposit Account"))

