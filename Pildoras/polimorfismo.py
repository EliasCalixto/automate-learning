class Coche():
    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')

class Moto():
    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')

class Camion():
    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')

miVehiculo = Moto()
miVehiculo2 = Coche()

miVehiculo.desplazamiento()
miVehiculo2.desplazamiento()
