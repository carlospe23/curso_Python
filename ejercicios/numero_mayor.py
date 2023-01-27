import random

# Generando numeros aleatorios
numeros = [random.randint(1, 100) for _ in range(1, 20)]

biggest_number = 0

for numero in numeros:
    if numero > biggest_number:
        biggest_number = numero
    
print(numeros)
print(max(numeros))
print(biggest_number)

