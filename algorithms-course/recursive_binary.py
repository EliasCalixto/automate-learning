def recursive_binary_search(lista,target):
    if len(lista)==0:
        return False
    else:
        midpoint = len(lista)//2
        if lista[midpoint]==target:
            return True
        elif lista[midpoint]<target:
            return recursive_binary_search(lista[midpoint+1:],target)
        elif lista[midpoint]>target:
            return recursive_binary_search(lista[:midpoint],target)

def verify(result):
    print('Target found:',result)

numbers = list(range(1,201))
result = recursive_binary_search(numbers,199)
verify(result)


