#primero se define la clase 'carro'
class Carro():
    #Aqui de definen las propiedades, las encapsulamos dentro de
    #la funcion '__init__'
    def __init__(self,marca, modelo): #pusimos marca y modelo como parametro para que al instanciar el objeto lo colocaramos manualmente.
        self.ruedas = 4
        self.largoChasis = 450
        self.anchoChasis = 250
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False #Esta variable va en False porque todo carro antes de usarse esta apagado.
    #Ahora aca van los comportamientos
    def arrancar(self):
        self.enMarcha = True

    def frenar(self):
        self.enMarcha = False

    def estado(self):
        print('El auto tiene:',self.ruedas,'ruedas.')
        print('Su marca es:',self.marca)
        print('Su modelo es:',self.modelo)
        if self.enMarcha == True:
            print('El auto esta en marcha.')
        else:
            print('El auto esta en apagado.')

#Ahora vamos a instanciar el objeto
miCarro = Carro('Toyota','1990')
#imprimimos un comportamiento, cambiamos el estado del auto, y mostramos el estado
miCarro.ruedas
miCarro.enMarcha
miCarro.arrancar()
miCarro.estado()


