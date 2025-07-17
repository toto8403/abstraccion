from abc import ABC, abstractmethod
class Empleado(ABC):
    @abstractmethod
    def calcular_sueldo(self):
        pass
class empleado_hora(Empleado):
    def calcular_sueldo(self, C, M):
        S=M/C
        print(f"el salario es: {S}")
class Empleado_fijo(Empleado):
    def calcular_sueldo(self, M, H):
        SH=300/H
        S=((SH*H)*57)/12
        print(f"el salario es: {S}")
if __name__=="__main__":
    potato=empleado_hora()
    a=int(input("ingrese la cantidad de horas idas al trabajo: "))
    potato.calcular_sueldo(a, 300)
    potato=Empleado_fijo()
    b=int(input("ingresa la cantidad de horas que trabajo: "))
    potato.calcular_sueldo(300, b)
