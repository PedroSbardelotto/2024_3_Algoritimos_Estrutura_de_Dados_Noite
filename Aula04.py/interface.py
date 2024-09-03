import sys

from PySide6.QtWidgets import QApplication, QPushButton
app = QApplication(sys.argv)

botao = QPushButton("Cadastre seu usuário")
botao.show() # Adicionar o widget na hierarquia eexibe a janela
botao.setStyleSheet('font-size:40px; color:red;')

botao2 = QPushButton("Texto do botão2")
botao2.show()# Adicionar o widget na hierarquia eexibe a janela


app.exec() # loop da aplicação
