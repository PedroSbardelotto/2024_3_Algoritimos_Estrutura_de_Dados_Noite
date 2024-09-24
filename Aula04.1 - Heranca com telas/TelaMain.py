from FormCliente import FormCliente
from Cidade import Cidade
import sys
from PyQt5.QtWidgets import QApplication
# from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel
from TelaPrincipal import TelaPrincipal
app = QApplication(sys.argv)
# telaProd = TelaProduto("Cadastro de Produto")
# telaProd.show()


# tp = TelaPrincipal()
# tp.show()
listcidades = []
listcidades.append(Cidade("Porto Alegre"))
listcidades.append(Cidade("Bento"))
formCli = FormCliente(pessoas=[], cidades=listcidades)

formCli.show()



sys.exit(app.exec_())
