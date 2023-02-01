import csv

with open('archivo') as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)