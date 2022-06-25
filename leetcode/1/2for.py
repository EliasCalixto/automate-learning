def twoFor(nums,tar):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==tar:
                return [i,j]

arr=[1,2,8,4,3]
target=11
print(twoFor(arr,target))