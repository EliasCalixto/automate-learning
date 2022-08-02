def linearSearch(length,target):
    arr = list(range(1,length+1))
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i

print(linearSearch(100,55))