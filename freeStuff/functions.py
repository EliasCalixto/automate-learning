A = int(input('Ingrese 2 numeros enteros: \n'))
B = int(input())
D = int(input('Ingrese otros 2 numeros enteros: \n'))
E = int(input())

def func(a,b):
    c = a + b
    return c

def funcjr(d,e):
    f = d + e
    return f

def lastfun():

    x = func(A,B)
    y = funcjr(D,E)
    print(x+y)
    return x + y

lastfun()

N = func(6,7)+funcjr(3,4)
M = N ** 2

print(N+M)

