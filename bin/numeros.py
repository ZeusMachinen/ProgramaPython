def numeros():
    a=float(input('Escribe el primer numero'))
    b=float(input('Escribe el segundo numero'))
    c=float(input('Escribe el tercer Numero'))
    if a>b and a>c:
        print('el mayor es {}'.format(a))
    elif b>a and b>c:
        print('el mayor es {}'.format(b))
    else:
        print('el mayor es {}'.format(c))