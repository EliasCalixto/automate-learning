def recursiveBinary(lista,target):
    if len(lista)==0:
        return False
    else:
        midpoint=len(lista)//2
        if lista[midpoint]==target:
            return True
        elif lista[midpoint]>target:
            return recursiveBinary(lista[:midpoint],target)
        elif lista[midpoint]<target:
            return recursiveBinary(lista[midpoint+1:],target)

nums=list(range(1,2000000+1))
print(recursiveBinary(nums,6))