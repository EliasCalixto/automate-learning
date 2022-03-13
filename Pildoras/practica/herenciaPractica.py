#Ahora repasare las herencias en los objetos.
class Computadora():
    def __init__(self,procesador,generacion):
        self.__procesador=procesador
        self.__generacion=generacion
        self.__ram='16gb'
        self.__encendido=False

    def encender(self):
        self.__encendido=True

    def reiniciar(self):
        self.__encendido=False
        self.__encendido=True

    def apagar(self):
        self.__encendido=False

    def estado(self):
        print('Procesador:',self.__procesador)
        print('Generacion:',self.__generacion)
        print('Ram:',self.__ram)
        print('Encendido:',self.__encendido)

class MyLap(Computadora):
    prueba = 1024

pc1 = MyLap('Intel','i5-10400f')

pc1.estado()
print(pc1.prueba)
