from Pessoa import Cidade
from Pessoa import Pessoa
from Pedido import Pedido
from Categoria import Categoria
from Produto import Produto

cid01 = Cidade()
cid02 = Cidade("Porto Alegre")

cli01 = Pessoa("Pedro")
cli02 = Pessoa("Maria", 1.82)
cli03 = Pessoa("josé", cid = cid01)



cat01 = Categoria()
cat02 = Categoria("Alimentos")

prod01 = Produto("Coca-cola")
prod02 = Produto("Fanta", 8.80)
prod03 = Produto("Arroz", 5.80, cat02)
prod04 = Produto("pepsi", categoria = cat01)

ped01 = Pedido("Rua A")
ped02 = Pedido("Rua B", cli02) #Maria 

print(ped01)
ped01.addProduto(prod01)
print(ped01.addProduto(prod02))

ped01.imprimir()

from perecivel import Perecivel

Prod01Per01 = Perecivel("Alface", 3.99, cat01, 10)
