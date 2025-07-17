from abc import ABC, abstractmethod
class Notificacion(ABC):
    @abstractmethod
    def enviar(self):
        pass
class Email(Notificacion):
    def enviar(self, prs_envio):
            print(f"se a enviado el mensaje a {prs_envio}")
class SMS(Notificacion):
    def enviar(self, prs_envio):
        print(f"se a enviado el mensaje a {prs_envio}")
if __name__=="__main__":
    potato=Email()
    a = input("Enviar a: ")
    potato.enviar(a)
    potato2=SMS()
    b=input("enviar a: ")
    potato2.enviar(b)
