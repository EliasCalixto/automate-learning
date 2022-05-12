def divide(n1,n2):
    try:
        res=n1/n2
        return res

    except:
        print('No puedes dividir por 0')
        return divide(5,2)

divide(9,0)
