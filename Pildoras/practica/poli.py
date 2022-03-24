class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def calcularSueldoAnual(self):
        self.sueldoAnual = self.sueldo*12*(1+1/100)
        print(f'El sueldo anual del empleado {self.nombre}, es de {self.sueldoAnual}$')

class Contable(Empleado):
    def __init__(self,nombre,sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldoAnual(self):
        self.sueldoAnual = self.sueldo*12*(1+4/100)
        print(f'El sueldo anual del contable {self.nombre}, es de {self.sueldoAnual}$')

class Publicista(Empleado):
    def __init__(self,nombre,sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldoAnual(self):
        self.sueldoAnual = self.sueldo*12*(1+5/100)
        print(f'El sueldo anual del publicista {self.nombre}, es de {self.sueldoAnual}$')

class Becario(Empleado):
    def __init__(self,nombre,sueldo):
        super().__init__(nombre, sueldo)

    def calcularSueldoAnual(self):
        self.sueldoAnual = self.sueldo*12
        print(f'El sueldo anual del becario {self.nombre}, es de {self.sueldoAnual}$')


empleados = [
    Empleado('Juan',1000),
    Contable('Miguel',1100),
    Publicista('Rxdrx',1200),
    Becario('Elias',750)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()
