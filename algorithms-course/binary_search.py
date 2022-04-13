import random
def binary_search(lista,target):
    first = 0
    last = len(lista) - 1
    intentos = 0
    while first <= last:
        midpoint = (first + last)//2
        if lista[midpoint] == target:
            print(intentos)
            return midpoint
        elif lista[midpoint] < target:
            first = midpoint + 1
            intentos += 1
        else:
            last = midpoint - 1
            intentos += 1

    return None

def verify(index):
    if index is not None:
        print('Target found at index:',index)
    else:
        print('Target not found in list')

numbers = list(range(0,10))

for i in range(1,11):
    verify(binary_search(numbers,random.randint(1,10)))


