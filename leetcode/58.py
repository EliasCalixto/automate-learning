def lengthOfLastWord(s: str) -> int:
    contador = 0
    word = ''
    for i in s[::-1]:
        if i != ' ':
            contador += 1
            word += i

    finalWord = word[::-1]
    print(f'La ultima palabra es {finalWord} y su largo es {contador}')

lengthOfLastWord('   llllelias es darkesthj     ')
