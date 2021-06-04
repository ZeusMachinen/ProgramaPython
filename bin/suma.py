def suma():
    print('escriba un numero')
    n= int(input())
    suma = 0
    for valor in range (1,n):
        suma = suma + valor
        print(valor,end ='+')
        suma+= n
        print(n,'=',suma)