def factorial():
    numero=int(input('Numero: '))
    factorial=1
    if numero!=0:
        for i in range(1,numero+1):
            factorial=factorial*i
    print('Factorial:',factorial)