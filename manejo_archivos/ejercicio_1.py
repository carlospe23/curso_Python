# escribir los nombres y apellidos de dos listas en un archivo

#dos listas una con nombres otra con apellidos
nombres = ['Pedro', 'Pablo', 'Carlos', 'Nathali', 'Luis']
apellidos = ['Torres', 'Leon', 'Reyes', 'Bautista', 'Pascal']


# Regostramdp esta omfpr,acopm em im txt de forma optima

with open('./Nombre_y_apellido.txt', 'a') as archivo:
    archivo.writelines('Los datos son:\n')
    [
        archivo.writelines(f' Nombre: {nombre}\n Apellido: {apellido}\n') 
        for nombre, apellido in zip(nombres,apellidos)
    ]