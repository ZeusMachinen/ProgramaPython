def capital():
    c=float(input('Escribe el capital inicial: '))
    while c<0:
        c=float(input('El capital debe ser positivo: '))
    m=0
    p=c
    while c<=2*p:
        c=c+0.05*c
        m=m+1
    print('El numero de meses en el que se duplico el capital es {}'.format(m))