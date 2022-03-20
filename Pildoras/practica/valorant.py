class Armas():
    def __init__(self,tipo,nombre,d_cabeza,d_cuerpo,d_pies,cant_balas):
        self.tipo = tipo
        self.nombre = nombre
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
        print('Tipo:',self.tipo,'\nNombre:',self.nombre,'\nDano Cabeza:',self.d_cabeza,'\nDano Cuerpo:',self.d_cuerpo,'\nDano Piernas:',self.d_pies,'\nCantidad Balas:',self.cant_balas,'\nApuntando:',self.apuntando,'\nBalas Actuales:',self.balas)

Vandal = Armas('Primaria','Vandal',150,39,28,25)
