lista = [1,2,3]
anterior = lista[0]
print (anterior)
for cadanumero in range(0,len(lista)-1):
    suma = lista[cadanumero+1] + anterior
    print (suma)
    anterior = suma
