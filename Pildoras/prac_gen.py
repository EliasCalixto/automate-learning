myWord = 'Elias asd asd'

def generaLetras(palabra):
        yield palabra

generador = generaLetras(myWord)

print(next(generador))
print(next(generador))
