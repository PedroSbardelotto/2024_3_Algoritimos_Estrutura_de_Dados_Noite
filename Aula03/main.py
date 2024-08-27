from Pessoa import Cidade
from Pessoa import Pessoa
from Pedido import Pedido
from Categoria import Categoria


cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

cli01 = Pessoa("Pedro")
cli02 = Pessoa("Maria", 1.82)
cli03 = Pessoa("josé", cidade = cid01)



