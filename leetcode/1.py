def twoSum(nums,target):
    prevMap = {} #index : val
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
        print(prevMap)
    return 

print(twoSum([3,2,3],6))