def pelota():
    while True:
        try:
            altura=int(input('Escribe la altura: '))
            if altura<0:
                altura=float(input('La altura debe ser positiva, ingresa una nuevamente: '))
        except:
            print('el numero debe ser un numero  R+, ingrese uno nuevamente')
        else:
            break
    return altura