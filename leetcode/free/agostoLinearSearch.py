def linearSearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    return None

myList = [100,101,102,103,104,105,7,107,108,109]

print(linearSearch(myList,7))