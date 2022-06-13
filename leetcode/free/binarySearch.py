def binarySearch(lista:list,target:int) -> int:
    first=0
    last=len(lista)-1
    tries=0
    while first<=last:
        midpoint=(first+last)//2
        if lista[midpoint] == target:
            tries+=1
            print(tries)
            return midpoint
        elif lista[midpoint]>target:
            tries+=1
            last=midpoint-1
        elif lista[midpoint]<target:
            tries+=1
            first=midpoint+1
    return None

nums=list(range(1,300020000+1))
print(binarySearch(nums,700))