# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(955, 851)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 191, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 141, 41))
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(90, 690, 651, 91))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(340, 60, 321, 191))
        self.groupBoxIceCreams.setCheckable(True)
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.checkBoxChocolateChips = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateChips.setGeometry(QtCore.QRect(30, 50, 201, 23))
        self.checkBoxChocolateChips.setObjectName("checkBoxChocolateChips")
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxCookieDough.setGeometry(QtCore.QRect(30, 80, 171, 23))
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.checkBoxChocolateAlmond = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateAlmond.setGeometry(QtCore.QRect(30, 110, 171, 23))
        self.checkBoxChocolateAlmond.setObjectName("checkBoxChocolateAlmond")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxRockyRoad.setGeometry(QtCore.QRect(30, 140, 181, 23))
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(280, 340, 241, 201))
        self.groupBoxDrinks.setCheckable(True)
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(10, 40, 92, 23))
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setGeometry(QtCore.QRect(10, 70, 92, 23))
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setGeometry(QtCore.QRect(10, 110, 92, 23))
        self.checkBoxTea.setObjectName("checkBoxTea")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCreams"))
        self.checkBoxChocolateChips.setText(_translate("Dialog", "Mint Chocolate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChocolateAlmond.setText(_translate("Dialog", "Chocolate Almond $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

