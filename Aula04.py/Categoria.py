class Categoria: 
    def __init__(self, nome = "Bebidas") -> None:
        self.id = None 
        self.nome = nome

    def __str__(self) -> str:
        return f" - Nome: {self.nome}"
    