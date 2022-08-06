def es_bisiesto(numero):
    if numero %400 ==0:
        print(f'{numero} es bisiesto')
    elif numero%100==0:
        print(f'{numero} no es bisieto')
    elif numero %4==0:
        print(f'{numero} es bisiesto')
    else:
        print(f'{numero} no es bisiento')
numero=2019