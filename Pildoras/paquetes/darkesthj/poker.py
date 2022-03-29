import random

def poker():
    cartas=['Ah','Kh','Qh','Jh','Th','9h','8h','7h','6h','5h','4h','3h','2h',
            'As','Ks','Qs','Js','Ts','9s','8s','7s','6s','5s','4s','3s','2s',
            'Ac','Kc','Qc','Jc','Tc','9c','8c','7c','6c','5c','4c','3c','2c',
            'Ad','Kd','Qd','Jd','Td','9d','8d','7d','6d','5d','4d','3d','2d']

    carta1=cartas[random.randint(0,len(cartas)-1)]
    cartas.remove(carta1)
    carta2=cartas[random.randint(0,len(cartas)-1)]
    cartas.remove(carta2)

    mano = carta1+carta2
    print(mano)

poker()
poker()
poker()
poker()
poker()
poker()
poker()
poker()
poker()
poker()
poker()
