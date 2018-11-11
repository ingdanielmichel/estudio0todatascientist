def duplicado(array):
    nueva_lista = list(set(array))
    if len(nueva_lista) == len(array):
        return True

array =[1,2,3,2]
duplicado(array)
