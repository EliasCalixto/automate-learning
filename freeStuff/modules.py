import random

def asd():   
    a = random.randint(2,6)
    b = random.randint(1,4)
    c = a**b
    print(c)

    if c < 1000:
        asd()

asd()

















