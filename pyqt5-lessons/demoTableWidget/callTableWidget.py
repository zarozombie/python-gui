import sys
from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem
from DemoTableWidget import *
class MyForm(QDialog):
    def __init__(self,data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.data=data
        self.addcontent()
    def addcontent(self):
        row=0
        col=0
       # data=[]
        self.data.append(('Ordinary', '10'))
        self.data.append(('Super Deluxe', '20'))
        self.data.append(('Super Luxury', '30'))
        self.data.append(('Suite', '40'))
        
        for tup in self.data:
            col=0
            for item in tup:
                oneitem=QTableWidgetItem(item)
                self.ui.tableWidget.setItem(col, row, oneitem)
                col+=1
                row+=1
                print(col,row,item)
if __name__=="__main__":
    app = QApplication(sys.argv)
    data = []
    w = MyForm(data)
    w.show()
    sys.exit(app.exec_())
