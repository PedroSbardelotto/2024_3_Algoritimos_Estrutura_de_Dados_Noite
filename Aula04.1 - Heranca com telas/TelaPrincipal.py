import sys
#from PyQt5 import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import *

class TelaProduto(QMainWindow):
    def __init__(self, titulo="Lojinha Do Pedro"):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(300, 200, 200, 300)
        self.layout = QVBoxLayout()

    def definiLayout(self):
        self.btnCidade = QPushButton('Add Produto')
        self.btnCliente = QPushButton('Add Cliente')