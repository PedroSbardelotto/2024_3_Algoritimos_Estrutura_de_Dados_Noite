from .Categoria import Categoria
from Produto import Produto

class Perecivel(Produto):
        def __init__(self, nome, preco, categoria,temperatura) -> None:
                super().__init__(nome, preco, categoria)
                self.temperatura = temperatura
        def __str__(self) -> str:
                txt = super().__str__()
                txt += "\nTemperatura" + str(self.temperatura)
                return