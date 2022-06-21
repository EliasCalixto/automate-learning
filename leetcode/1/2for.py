def twoFor(nums,tar):
    for i in range(len(nums)-1):
        for j in nums:
            if nums[i]+nums[i+1]==tar:
                return [i,i+1]

arr=[9,2,3,5,1]
target=10
print(twoFor(arr,target))