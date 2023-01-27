frase = input('Dime una frase y te calculo cuanto tardarias si tuvieras que decirla: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)
print(f'dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo')