from Categoria import Categoria

class Produto:
    def __init__(self, nome:str, preco = 0.0, categoria = Categoria("outra")) -> None:
        self.id = None
        self.nome = nome
        self.preco = preco
        self.categoria = categoria