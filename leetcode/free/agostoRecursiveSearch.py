def recursiveSearch(array: list,target: int) -> int:
    first = 0
    last = len(array)
    while first <= last:
        midpoint = (first + last)//2
        if array[midpoint] == target:
            return midpoint
        elif array[midpoint] > target:
            last = midpoint-1
        elif array[midpoint] < target:
            first = midpoint+1
    return None
myList = list(range(0,1001))
print(recursiveSearch(myList,1002))