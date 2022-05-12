correo = input('Ingrese su correo electronico: ')

arroba = correo.count('@')

if arroba!=1 or correo.rfind('@')==len(correo)-1 or correo.find('@')==0:
    print('Mail Incorrecto')

else:
    print('Mail Correcto')



