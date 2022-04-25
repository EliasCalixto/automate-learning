def lengthOfLastWord(s:str) -> int:
    i = len(s)-1
    contador = 0
    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        contador += 1
        i -= 1
    return contador

print(lengthOfLastWord(' darkesthj es elias asdasd   '))