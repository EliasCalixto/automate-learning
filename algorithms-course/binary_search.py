import random
def binary_search(lista,target):
    first = 0
    last = len(lista) - 1
    while first <= last:
        midpoint = (first+last)//2
        if lista[midpoint] == target:
            return midpoint
        elif lista[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print('Target found at index:',index)
    else:
        print('Target not founj in list')

numbers = list(range(11))

for i in range(5):
    verify(binary_search(numbers,random.randint(0,11)))


