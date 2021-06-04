def ciudad():
    año=1980
    ciudad_a=3500000
    ciudad_b=5000000
    interes_a=0.07
    interes_b=0.05
    while ciudad_a<ciudad_b:
        ciudad_a=ciudad_a+(ciudad_a*interes_a)
        ciudad_b=ciudad_b+(ciudad_b*interes_b)
        año=año+1
    if año==1999:
        print('el año en el que la ciudad a pasa a la ciudad b es {}:'.format(año))