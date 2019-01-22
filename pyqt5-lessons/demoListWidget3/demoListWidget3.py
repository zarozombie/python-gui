# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(851, 399)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 170, 17))
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(190, 50, 210, 25))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(150, 110, 89, 25))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidgetSelectedItem = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItem.setGeometry(QtCore.QRect(420, 50, 360, 260))
        self.listWidgetSelectedItem.setObjectName("listWidgetSelectedItem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Favorite Food Item"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add to List"))

