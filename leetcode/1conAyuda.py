def linearSearch(length,target):
    arr = list(range(1,length+1))
    for i in arr:
        if arr[i-1]==target:
            return i-1
    return None
print(linearSearch(100,100))