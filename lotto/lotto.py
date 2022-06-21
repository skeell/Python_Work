#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import random as rnd
 

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)

    def estr1(self):
        c = rnd.randint(1,90)
        c = str(c)
        self.lb1.setText(c)

    def estr2(self):
        c = rnd.randint(1,90)
        c = str(c)
        self.lb2.setText(c)
    
    def estr3(self):
        c = rnd.randint(1,90)
        c = str(c)
        self.lb3.setText(c)
    
    def estr4(self):
        c = rnd.randint(1,90)
        c = str(c)
        self.lb4.setText(c)

    def estr5(self):
        c = rnd.randint(1,90)
        c = str(c)
        self.lb5.setText(c)


app = QApplication([])
window = Ui()
window.show()
app.exec()
