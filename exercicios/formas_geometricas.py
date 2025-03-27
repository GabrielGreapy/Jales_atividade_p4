import math
class FormaGeometrica:
    def calcular_perimetro(self):
        return None
        

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_perimetro(self):
        return self.largura * self.altura


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_perimetro(self):
        return math.pi * self.raio ** 2
 

circulo1 = Circulo(5)
circulo2 = Circulo(7)
retangulo1 = Retangulo(10, 15)
retangulo2 = Retangulo(15, 20)

lista = [circulo1, circulo2, retangulo1, retangulo2]

for i in lista:
    print(i.calcular_perimetro())