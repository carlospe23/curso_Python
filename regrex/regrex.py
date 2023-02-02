import re

texto = """Hola maestro, esta es la cadena 1. como estas mi capitan
    Esta es la segunda linea de texto 223 
    y Esta es la fina definitiva 3 mi capitan"""

resultado = re.search("Hola", texto)
#\d => busca digitos numericos del 0 al 9
resultado = re.findall(r'\d', texto)
# \D => busca TODO MENOS digitos numericos 
resultado = re.findall(r'\D', texto)

# w => busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r'\w', texto)

# W => busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r'\W', texto)

# s => busca espacios en blanco => espacios, tabs, saltos de linea
resultado = re.findall(r'\s', texto)

# S => busca TODO MENOS espacios en blanco => espacios, tabs, saltos de linea
resultado = re.findall(r'\S', texto)

# . => Busca TODO MENOS saltos de linea
resultado = re.findall(r'.', texto)

# \n => Busca saltos de linea
resultado = re.findall(r'\n', texto)

# \. => Cancela caracteres especiales, cancela la funcion del punto y busca puntos
resultado = re.findall(r'\.', texto)

#armando una cadena que busque un numero, seguido de un punto y un espacop
resultado = re.findall(r'\d\.\s', texto)

#busca el principio de una linea
# ^ -> busca el comienzo de una linea
resultado = re.findall(r'^Hola', texto)

#busca el principio de una linea
# lo mismo de arriba pero con flags
resultado = re.findall(r'^Hola', texto, flags=re.M)

#busca el principio de una linea
# $ -> busca el final de una linea
resultado = re.findall(r'capitan$', texto)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}', texto)

#{n} -> busca n cantidad de veces el valor de la izquierda y un espacio
resultado = re.findall(r'\d{3}\s', texto)

#{n, m} -> almenos n, como maximo m
resultado = re.findall(r'\d{1,2}', texto)

# | busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola', texto)

print(resultado)