me = ['elias','calixto','salazar','darkesthj']

he = ['enzo','gianolli','occonor','timado','10k','undying']

w = 'eliasdasdasdasdasd'

def comma(a):
    n = 0
    while len(a) > n + 1:
        print(a[n]+', ', end='')
        n += 1
    print('and '+a[n])



comma(me)
comma(he)
comma(w)

