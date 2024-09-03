from Produto import Produto
from Pessoa import Pessoa
from Categoria import Categoria
class Pedido:
    def __init__(self, end, cliente = Pessoa("Cliente não informado")) -> None:
        self.id = None 
        self.end = end
        self.cliente = cliente
        self.__prdutos = []
        


    def addProduto(self, prod) -> float:
        if prod is not None:
            self.__prdutos.append(prod)
        total = 0.0
        for p in self.__prdutos:
            total += p.preco
        return total

    def __str__(self) -> None:
        txt = f"Produtos:\n  "
        for p in self.__prdutos:
            txt += "\n-----------------------"
            txt += "\nNome: " + p.nome
            txt += "\nPreco: " + str(p.preco)
          # txt += "\nCategoria: " + p.categoria.nome
            txt += "\nCategoria: " + str(p.categoria)
        return txt
    