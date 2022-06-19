def twoSum(nums: list[int],target: int) -> list[int]:
    seen={}
    for i,num in enumerate(nums):
        if target-num in seen:
            return [seen[target-num,i]]
        elif num not in seen:
            seen[num]=i

arr = [2,3,4,9]
tar = 11

print(twoSum(arr,tar))