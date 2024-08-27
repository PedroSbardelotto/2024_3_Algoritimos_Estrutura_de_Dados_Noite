from Cidade import Cidade
class Pessoa:
    def __init__(self, id:int, nome:str, altura = 1.73, cid = Cidade("Itati")) -> None:
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = cid 