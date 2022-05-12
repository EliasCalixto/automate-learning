def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subelemento in elemento:
            yield from elemento

ciudades_devueltas=devuelveCiudades('Madrid','Barcelona','Bilbao','Valencia')

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))