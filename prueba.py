def complejidad(lista):
    for x in lista:
        if x == 33:
            print('Esto es lo que buscamos!')
            return(x)
        print('No esta lo que buscamos')

def simplicidad(lista):
    if len(lista)>0:
        print('Tenemos datos!')
        return
    print('No tenemos datos!')
    return


lista = [1,21,23,321,43,245,431,534,33,231,23,123,21]
complejidad(lista)
simplicidad(lista)
