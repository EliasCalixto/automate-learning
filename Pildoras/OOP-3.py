class Coche():
    #propierties
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    #behaviors
    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if(self.enMarcha):
            return 'El coche esta en marcha'
        else:
            return 'El coche esta parado'

miCoche = Coche()

print('----------------------- Segundo Objeto ---------------------------')

miCoche2 = Coche()
print('El largo del coche es: ',miCoche.largoChasis)
print('El coche tiene ', miCoche.ruedas,' ruedas')










