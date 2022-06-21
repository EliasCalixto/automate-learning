def searchAsd(lst,obj):
    getted={}
    for i,num in enumerate(lst):
        if obj-num in getted:
            return [getted[obj-num],i]
        else:
            getted[num]=i

lista=[2,3,4,1,5,6]
objetivo=11
print(searchAsd(lista,objetivo))