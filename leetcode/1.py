def twoSum(nums,target):
    output=[]
    i1=0
    i2=1
    while(nums[i1]+nums[i2])!= target and i1!=i2:
        i1+=1
        i2+=1


    output.append(i1)
    output.append(i2)
    return output

n=[1,2,3,5]
print(twoSum(n,8))