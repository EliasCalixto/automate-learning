MY_PETS = ['Zophie','Pooka','Fat-tail']
MY_PETS = MY_PETS + ['Bella']
print('Enter a pet name: ')
name = input()
if name not in MY_PETS:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')



















