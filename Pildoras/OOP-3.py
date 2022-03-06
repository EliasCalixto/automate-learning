class Coche():
    #propierties
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    #behaviors
    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if (self.enMarcha):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

    def estado(self):
        print('El coche tiene ', self.ruedas, 'ruedas. Un ancho de ', self.anchoChasis, 'y un largo de ', self.largoChasis)

miCoche = Coche()
print('El largo del coche es: ', miCoche.largoChasis)
print('El coche tiene ', miCoche.ruedas, 'ruedas')
print(miCoche.arrancar(True))
miCoche.estado()

print('----------------------- Segundo Objeto ---------------------------')

miCoche2 = Coche()
print('El largo del coche es: ',miCoche.largoChasis)
print('El coche tiene ', miCoche.ruedas,' ruedas')
print(miCoche.arrancar(False))
miCoche2.estado()
