from bin.capital import capital
from bin.numeros import numeros
from bin.multiplos import multiplos
from bin.fibonacci import fibonacci
from bin.rebotes import rebotes
from bin.pelota import pelota
from bin.ciudad import ciudad
from bin.primo import primo
from bin.suma import suma
from bin.factorial import factorial

def menu():
    print('¿Que opcion del menu desea hacer?')
    print('1.La capital')
    print('2.Tres numeros y indicar numero mayor')
    print('3.ejercicio de la pelota')
    print('4.Ciudad A y B')
    print('5.serie fibonacci')
    print('6.Multiplos de 7 y 9')
    print('7.Numero primo')
    print('8.Factorial de un numero')
    print('9.Diagrama de sumatoria')
    print('10.Salir')
    opc = int(input("Qué opción desea hacer? "))
    while opc != 10:
        if opc == 1:
            capital()
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 2:
            numeros()
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 3:
            a = pelota()
            rebotes(a)
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 4:
            ciudad()
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 5:
            fibonacci()
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 6:
            multiplos()
            opc = int(input("Qué opción desea ahora? "))
        elif opc == 7:
            primo()
            opc = int(input("Qué opción desea ahora? "))
        elif opc==8:
            factorial()
            opc=int(input("Qué opción desea ahora? "))
        elif opc==9:
            suma()
            opc=int(input("Qué opción desea ahora? "))
        else:
            print("La opcion ingresa no es valida, Digita otra")       
menu()




