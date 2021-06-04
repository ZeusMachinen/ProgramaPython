def multiplos():
    x=0
    y=0
    for i in range(1000, 5000):
       if(i % 9 == 0):
           x += 1
       if(i % 7 == 0):
           y += 1           

    print("multiplos de 7: {}".format(y))       
    print("multiplos de 9: {}".format(x))