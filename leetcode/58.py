def lengthOfLastWord(s: str) -> int:
    i = len(s)-1
    length = 0
    while s[i]==' ':
        i-=1
    while s[i]!=' ':
        length+=1
        i-=1
    return length
print(lengthOfLastWord(' asdf adfl darkesthj sf darkesthj   '))
print('kkx')