class PC():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.ram = 16
        self.encendido = False
        
    def encender(self):
        self.encendido = True

    def apagar(self):
        self.encendido = False
    
    def reiniciar(self):
        self.encendido = False
        self.encendido = True

    def estado(self):
        print('Marca:',self.marca)
        print('Modelo:',self.modelo)
        print('Ram:',self.ram)
        print('Encendido:',self.encendido)

class Ryzen(PC):
    pass

class Intel(PC):
    pass

pc1 = Ryzen('AMD','Ryzen5 3400g')
pc2 = Intel('Intel','i5-10400f')

pc1.estado()
pc2.encender()
pc2.estado()

