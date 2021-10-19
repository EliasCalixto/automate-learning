CAT_NAMES = []
while True:
    print('Enter the name of cat '+ str(len(CAT_NAMES) + 1) +
          ' (Or enter nothing to stop.): ')

    name = input()
    if name == '':
        break
    CAT_NAMES = CAT_NAMES + [name]

print('The cat names are: ')
for name in CAT_NAMES:
    print('  '+name)




















