import pickle

class Vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True
        
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print('marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enMarcha, '\nAcelerando: ', self.acelera, '\nFrenando: ', self.frena)

coche1=Vehiculos('Mazda','MX6')
coche2=Vehiculos('Seat','DGH3')
coche3=Vehiculos('Renault','3DE')

coches = [coche1,coche2,coche3]

fichero = open('losCoches','wb')

pickle.dump(coches,fichero)

fichero.close()

del fichero

ficheroApertura = open('losCoches','rb')

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for i in misCoches:
    print(i.estado())






