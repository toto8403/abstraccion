from abc import ABC, abstractmethod
import math
class Figura:
    @abstractmethod
    def calcular_area(self):
        pass
class Circulo(Figura):
    def calcular_area(self, radio):
        AREA=3,1415*(radio ** 2)
        print(f"el area del circulo es: {AREA}")
class Rectangulo(Figura):
    def calcular_area(self, base, altura):
        AREA=base*altura
        print(f"el area del recangulo es: {AREA}")
potato = Circulo()
potato.calcular_area(5)
potato = Rectangulo()
potato.calcular_area(5, 10)
