# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 584)
        self.labelSelected = QtWidgets.QLabel(Dialog)
        self.labelSelected.setGeometry(QtCore.QRect(120, 490, 501, 61))
        self.labelSelected.setText("")
        self.labelSelected.setObjectName("labelSelected")
        self.VBoxLayout = QtWidgets.QSplitter(Dialog)
        self.VBoxLayout.setGeometry(QtCore.QRect(20, 10, 291, 201))
        self.VBoxLayout.setOrientation(QtCore.Qt.Vertical)
        self.VBoxLayout.setObjectName("VBoxLayout")
        self.label = QtWidgets.QLabel(self.VBoxLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setProperty("VBoxLayout", "")
        self.label.setObjectName("label")
        self.radioButtonMedium = QtWidgets.QRadioButton(self.VBoxLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonMedium.setFont(font)
        self.radioButtonMedium.setProperty("VBoxLayout", "")
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.radioButtonLarge = QtWidgets.QRadioButton(self.VBoxLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonLarge.setFont(font)
        self.radioButtonLarge.setProperty("VBoxLayout", "")
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.radioButtonXL = QtWidgets.QRadioButton(self.VBoxLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonXL.setFont(font)
        self.radioButtonXL.setProperty("VBoxLayout", "")
        self.radioButtonXL.setObjectName("radioButtonXL")
        self.radioButtonXXL = QtWidgets.QRadioButton(self.VBoxLayout)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonXXL.setFont(font)
        self.radioButtonXXL.setProperty("VBoxLayout", "")
        self.radioButtonXXL.setObjectName("radioButtonXXL")
        self.VBoxLayout_2 = QtWidgets.QSplitter(Dialog)
        self.VBoxLayout_2.setGeometry(QtCore.QRect(30, 270, 288, 114))
        self.VBoxLayout_2.setOrientation(QtCore.Qt.Vertical)
        self.VBoxLayout_2.setObjectName("VBoxLayout_2")
        self.label_2 = QtWidgets.QLabel(self.VBoxLayout_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(self.VBoxLayout_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonDebitCard.setFont(font)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.VBoxLayout_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonNetBanking.setFont(font)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.VBoxLayout_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButtonCashOnDelivery.setFont(font)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose Your Shirt Size"))
        self.radioButtonMedium.setText(_translate("Dialog", "M"))
        self.radioButtonLarge.setText(_translate("Dialog", "L"))
        self.radioButtonXL.setText(_translate("Dialog", "XL"))
        self.radioButtonXXL.setText(_translate("Dialog", "XXL"))
        self.label_2.setText(_translate("Dialog", "Choose your Payment Method"))
        self.radioButtonDebitCard.setText(_translate("Dialog", "Debit / Creadit Card"))
        self.radioButtonNetBanking.setText(_translate("Dialog", "NetBanking"))
        self.radioButtonCashOnDelivery.setText(_translate("Dialog", "Cash on Delivery"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

