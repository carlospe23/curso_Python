try:
    lista = [1,2]
    print(lista[9])
except IndexError as e:
    print(e)
    print('ese indice no existe en la lista')