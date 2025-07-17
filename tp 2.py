from abc import ABC, abstractmethod
class Pago(ABC):
    @abstractmethod
    def procesar_pago(self):
        pass
class tarfetacredito(Pago):
    def procesar_pago(self,dinero):
        print(f"se a procesado el pago de {dinero}")
class paypal(Pago):
    def procesar_pago(self, dinero):
        print(f"se a procesado el pago de {dinero}")
if __name__=="__main__":
    potato=tarfetacredito()
    potato.procesar_pago(2000)
    potato2=paypal()
    potato2.procesar_pago(3000)
