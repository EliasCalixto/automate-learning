def lengthOfLastWord(s: str) -> int:
    i = len(s)-1
    length = 0
    word = ''
    
    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        word += s[i]
        i -= 1

    finalWord = word[::-1]
    print(finalWord)
    return length


print(lengthOfLastWord('   llllelias es darkesthj     '))
