import random

numeros = [random.randint(1, 100) for _ in range(1, 20)]

temporal = 0

for recorrido_1 in range(1, len(numeros)):
    for recorrido_2 in range(len(numeros) - recorrido_1):

        if numeros[recorrido_2] > numeros[recorrido_2 + 1]:
            temporal = numeros[recorrido_2]
            numeros[recorrido_2] = numeros[recorrido_2 + 1]
            numeros[recorrido_2 + 1] = temporal

print(numeros)