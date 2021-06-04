def primo():
    x= int(input("Escribe un numero: "))
    cont = 0
    if x < 1:
        print("el 1 no es primo")
    for i in range(1, x+1):
        if x % i == 0:
            cont+=1;
    if cont == 2:
        print("El {} es primo".format(x))
    elif cont !=2:
        print("El {} no es primo".format(x))
       

