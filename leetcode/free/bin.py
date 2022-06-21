def binary(nms,tar):
    first = 0
    last = len(nms)-1
    while first<=last:
        midpoint=(first+last)//2
        if nms[midpoint]==tar:
            return midpoint
        elif nms[midpoint]>tar:
            last=midpoint-1
        elif nms[midpoint]<tar:
            first=midpoint
    return None

nums=[10,11,12,13,14,15,16,17,18,19]
print(binary(nums,14))