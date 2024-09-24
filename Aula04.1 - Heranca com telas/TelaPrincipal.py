import sys
from PyQt5.QtWidgets import *
from FormCidade import FormCidade
from Cidade import Cidade


class TelaPrincipal(QMainWindow):
    def __init__(self, titulo="Lojinha Do Pedro"):
        super().__init__()

        self.setWindowTitle(titulo)
        self.setGeometry(100, 50, 200, 200)
        self.layout = QVBoxLayout()

        self.cidades = []
        self.clientes = []

        self.definirLayout()

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


def definirLayout(self):
    self.btnAddCidade = QPushButton("Add Cidade", self)
    self.btnAddCidades = QPushButton("ver cidades")

    self.btnAddCidades.clicked.connect(self.listarCidades)
    self.btnAddCidade.clicked.connect(self.addcidade)

    self.layout.addWidget(self.btnVercidades)
    self.layout.addWidget(self.btnVercidade)


def addCidade(self):
    app = QApplication(sys.argv)
    telaAddCidade = FormCidade(cidades=self.cidades)
    telaAddCidade.show()
    sys.exit(app.exec_())


def listarCidades(self):
    txt = ""
    if self.cidades.__len__() == 0:
        txt += "Nenhuma Cidade Cadastrada"
    else:
        for cid in self.cidades:
            txt += "\n" + cid.nome

    QMessageBox.information(self, "Lista de Cidades", txt)
