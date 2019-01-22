import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from demoCheckBox2 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxChocolateAlmond.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxChocolateChips.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxCookieDough.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxRockyRoad.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxCoffee.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSoda.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxTea.stateChanged.connect(self.dispAmount)
        self.show()
    def dispAmount(self):
        amount=0
        if self.ui.checkBoxChocolateAlmond.isChecked()==True:
            amount=amount+3
        if self.ui.checkBoxChocolateChips.isChecked()==True:
            amount=amount+4
        if self.ui.checkBoxCookieDough.isChecked()==True:
            amount=amount+2
        if self.ui.checkBoxRockyRoad.isChecked()==True:
            amount=amount+5
        if self.ui.checkBoxCoffee.isChecked()==True: 
            amount=amount+2
        if self.ui.checkBoxSoda.isChecked()==True:
            amount=amount+3
        if self.ui.checkBoxTea.isChecked()==True:
            amount=amount+1
        self.ui.labelAmount.setText("Total amount dispAmount $ " +str(amount))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
