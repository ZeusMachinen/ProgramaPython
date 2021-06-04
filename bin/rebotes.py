def rebotes(a):
    rebotes=0
    guardar_altura=a
    while a>=guardar_altura/5:
        a=a-(0.1*a)
        rebotes=rebotes+1
    print('la cantidad de rebotes fueron{}: '.format(rebotes)) 