"""
Exercício
▷ Construa um algoritmo para implementar a
classe Retângulo que possui os atributos: altura
e largura.
▷ A classe deve ter os seguintes métodos:
○ Método construtor
○ Método que calcula a área do retângulo
( altura * largura) e retorna o resultado
○ Método que imprime os valores dos atributos
da classe

"""

class Retangulo:
    def __init__(self) -> None:
        self.altura = None
        self.largura = None
    
    def calcula_area(self,altura:float, largura:float) -> int:
         area = altura * largura
         return f"Area do retangulo: {area}"
    
    
    def __str__(self, altura, largura) -> str:
        return f"Altura: {altura} \nLargura: {largura} "
    


teste = Retangulo()
#imprimindo os valores do retangulo
print(teste.__str__(10,9))
#calculando a area do retangulo
print(teste.calcula_area(10, 9))

