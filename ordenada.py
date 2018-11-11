def ordenada(array):
    z=0
    orden = True
    for x in range (0,len(array)-1):
        z=z+1
        if array[z] > array[x]:
            print(array[x], "es menor que", array[z])
            print (str(orden))
        else:
            print(array[x],"es MAYOR que " , array[z])
            orden = False
            print (str(orden))


array =[1,2,3,2]
ordenada(array)
