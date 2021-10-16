def in_X(): 
    global X
    try:
        X = int(input('Ingrese un numero entero: '))
        print(collatz(X))
    except:
        print('Ese no es un numero entero.')
        in_X()

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

in_X()





















