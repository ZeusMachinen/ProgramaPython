def fibonacci():
    print('La serie fibonacci para numeros menores a 1000')
    numero=int(input('Numero para la serie:'))
    while numero>=1000:
        numero=int(input('debe ser menor a 1000, digita otro:'))
        break
    a=0
    b=1
    for i in range(numero):
        print (a)
        c=a+b
        a=b
        b=c