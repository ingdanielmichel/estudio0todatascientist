
def sumadelista(array):
    lista = array
    anterior = lista[0]
    print (anterior)
    for cadanumero in range(0,len(lista)-1):
        suma = lista[cadanumero+1] + anterior
        print (suma)
        anterior = suma

def elimina(array):
    lista1  = array
    del lista1[0]
    del lista1[-1]
    print (lista1)

def ordenada(array):
    z=0
    for x in range (0,len(array)-1):
        z=z+1
        if array[z] > array[x]:
            orden = True
            #print (str(orden))
        else:
            orden = False
            #print (str(orden))
    return(orden)

def elimina_duplicados(array):
    nueva_lista = list(set(array))
    print (nueva_lista)

def duplicado(array):
    nueva_lista = list(set(array))
    if len(nueva_lista) != len(array):
        #print(True)
        return True

array =[1,2,3,2]
sumadelista(array)
#elimina(array)
ordenada(array)
elimina_duplicados(array)
duplicado(array)
