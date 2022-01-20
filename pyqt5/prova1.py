from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class Ui(QWidget):
    def __init__(self):#costruttore
        super().__init__()#richiamo costruttore classe madre
        uic.loadUi('ui.ui', self)
        #self.btn.clicked.connect(self.prova)

    def prova(self):
        print('Prova')


app = QApplication([])
window = Ui()

window.show()
app.exec()


