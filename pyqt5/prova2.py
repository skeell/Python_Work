from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class Ui(QWidget):
    def __init__(self):#costruttore
        super().__init__()#richiamo costruttore classe madre
        uic.loadUi('ui1.ui', self)
        #self.btn.clicked.connect(self.prova)

    def pB_moltiplicaClick(self):
        try:
            n1=int(self.lE_primoNumero.text())
            n2=int(self.lE_secondoNumero.text())
            self.lE_risultato.setText(str(n1*n2))
            self.l_comunicazione.setText('')
        except:
            self.lE_risultato.setText('')
            self.l_comunicazione.setText('Non ha inserito un numero valido')


app = QApplication([])
window = Ui()

window.show()
app.exec()
