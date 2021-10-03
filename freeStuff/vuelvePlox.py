def andoSad(): 
    print('Porque estas sad si eres gozu?')
    answer = input()

    if answer == 'Si':
        print('No estes triste broo')
    elif answer == 'No':
        print('No estes triste bruh')
        whynot = input()
    else:
        print('Soy un bot, solo leo "Si" o "No" srry')
        andoSad()

andoSad()
