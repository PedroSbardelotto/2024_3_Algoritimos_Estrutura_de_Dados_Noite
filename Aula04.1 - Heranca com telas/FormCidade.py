import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from Cidade import Cidade


class FormCidade(QMainWindow):
    def __init__(self, titulo="Formulário de Cidade", cidades=[]) -> None:
        super().__init__()
        self.cidades = cidades

        self.setWindowTitle(titulo)
        self.setGeometry(350, 100, 200, 200)
        self.layout = QVBoxLayout()
        self.definirLayout()

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def definirLayout(self):
        self.lblNome = QLabel("Nome da cidade: ")
        self.QLineEdit(self)
        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        self.btnaSalvar = QPushButton("Salvar", self)
        self.btnaSalvar.clicked.connect(self.salvar)
        self.layout.addwidget(self.btnaSalvar)

    def salvar(self):
        if len(self.txtNome.text) > 0:
            cid = Cidade( self.txtNome.text)
            self.cidades.append( cid )
            
