otros_crusos_min = 2.5
otros_crusos_max = 7
otros_crusos_promedio = 4
dalto_curso = 1.5

#Duracion ed crudos
crudo_promedio = 5
crudo_dalto = 3.5


#Diferencia de duracion

diferencia_con_min = 100 - dalto_curso / otros_crusos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_crusos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_crusos_promedio * 100

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_crusos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


# Mostrando las difenrencias del ejercicio
print(f'este curso dura un {diferencia_con_min}% menos que el mas rapido')
print(f'este curso dura un {diferencia_con_max}% menos que el mas lento')
print(f'este curso dura un {diferencia_con_promedio}% menos que el promedio')

#Mostrando la cantidad de espacios que se remueven
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% del tiempo vacio')
print(f'este curso elimina el {tiempo_vacio_dalto}% del tiempo vacio')


