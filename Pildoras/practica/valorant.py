class Jugador():
    def __init__(self,nickname,rango,personaje):
        self.nickname = nickname
        self.rango = rango
        self.personaje = personaje
        self.creditos_iniciales = 800

class Armas():
    def __init__(self,nombre,precio,d_cabeza,d_cuerpo,d_pies,cant_balas):
        self.nombre = nombre
        self.precio = precio
        self.d_cabeza = d_cabeza
        self.d_cuerpo = d_cuerpo
        self.d_pies = d_pies
        self.cant_balas = cant_balas
        self.balas = cant_balas
        self.apuntando = False

    def disparar(self,n):
        if n <= self.balas:
            self.balas -= n
            print('Se dispararon',n,'balas.')
            print('Quedan',self.balas,'balas.')
        else:
            print('Se dispararon',self.balas,'balas.')
            self.recargar()

    def recargar(self):
        self.balas = self.cant_balas
        print('Se ha recargado, tienes',self.balas,'balas.')

    def apuntar(self):
        self.apuntando = True
        if self.apuntando == True:
            print('Estas apuntando')
        else:
            print('No estas apuntado')

    def estado(self):
        print('Nombre:',self.nombre,'\nPrecio:',self.precio,'\nDano Cabeza:',self.d_cabeza,'\nDano Cuerpo:',self.d_cuerpo,'\nDano Piernas:',self.d_pies,'\nCantidad Balas:',self.cant_balas,'\nApuntando:',self.apuntando,'\nBalas Actuales:',self.balas)

class ArmaPrimaria(Armas):
    def __init__(self,nombre_p,precio_p,d_cabeza_p,d_cuerpo_p,d_pies_p,cant_balas_p):
        super().__init__(nombre_p,precio_p,d_cabeza_p,d_cuerpo_p,d_pies_p,cant_balas_p)
        self.tipo = 'Arma Primaria'

    def estado(self):
        super().estado()
        print('Tipo:',self.tipo)

class ArmaSecundaria(Armas):
    def __init__(self,nombre_p,precio_p,d_cabeza_p,d_cuerpo_p,d_pies_p,cant_balas_p):
        super().__init__(nombre_p,precio_p,d_cabeza_p,d_cuerpo_p,d_pies_p,cant_balas_p)
        self.tipo = 'Arma Secundaria'

    def estado(self):
        super().estado()
        print('Tipo:',self.tipo)

Vandal = ArmaPrimaria('Vandal',2900,159,40,28,25)
Ghost = ArmaSecundaria('Ghost',500,101,25,15,12)


