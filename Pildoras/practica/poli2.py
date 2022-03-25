class Empleado():
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcularSueldoAnual(self):
        self.sueldoAnual = round(self.sueldo*12*(1+5/100),2)
        print(f'El sueldo anual del empleado {self.nombre} es {self.sueldoAnual}')

class Contador(Empleado):
    def __init__(self,nombre,sueldo):
        super().__init__(nombre,sueldo)

    def calcularSueldoAnual(self):
        self.sueldoAnual = round(self.sueldo*12*(1+10/100),2)
        print(f'El sueldo anual del contador {self.nombre} es {self.sueldoAnual}')

class Publicista(Empleado):
    def __init__(self,nombre,sueldo):
        super().__init__(nombre,sueldo)

    def calcularSueldoAnual(self):
        self.sueldoAnual = round(self.sueldo*12*(1+12/100),2)
        print(f'El sueldo anual del publicista {self.nombre} es {self.sueldoAnual}')

empleados = [
    Empleado('Juan',1000),
    Contador('Elias',1200),
    Publicista('Sahory',1500)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()



