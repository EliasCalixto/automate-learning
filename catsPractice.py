IDIOMAS = []
while True:
    print('Ingrese el idioma ' + str(len(IDIOMAS)+1) +' (Or enter nothing to stop.): ')
    idioma = input()
    if idioma == '':
        break
    IDIOMAS = IDIOMAS + [idioma]
print('Los idiomas que habla son: ')
for idioma in IDIOMAS:
    print(' '+idioma)












