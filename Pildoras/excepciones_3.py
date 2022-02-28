def evaluaEdad(edad):
    if edad<0:
        raise TypeError('No se permiten edades negativas')
    if edad<20:
        return 'eres muy joven'
    elif edad<40:
        return 'eres joven'
    elif edad<65:
        return 'eres maduro'
    elif edad<100:
        return 'Cuidate...'
    
print(evaluaEdad(-15))
