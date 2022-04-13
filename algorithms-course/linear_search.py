numbers = [1,2,3,4,5,6,7,8,9,10]

def linear_search(lista,target):
    #returns the index position of the targert if found, else returns None
    for i in range(0,len(lista)):
        if lista[i] == target:
            return i

def verify(index):
    if index is not None:
        print('Target found at index:',index)
    else:
        print('Target not found in list')

result = linear_search(numbers,6)
verify(result)

