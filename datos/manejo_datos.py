numbers = [1, 2, 3, 4, 5]

numbers_v2 = list(map(lambda i: i * 2, numbers))

print(numbers_v2)

numbers2 = [1, 2, 3, 4, 5]
numbers3 = [1, 2, 3]

result = list(map(lambda x, y:  x + y, numbers2, numbers3))
print(result)

# MAP EN DICCIONARIOS
items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

# FILTER NORMAL

numbers = [1,2,3,4,5]
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)

# FILTER CON DICCIONARIOS

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print(new_list)
print(len(new_list))

print(matches)
print(len(matches))

# REDUCE 

import functools

numbers = [1, 2, 3, 4]

def accum(counter, item):
  print('counter => ',counter)
  print('item => ',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)

#EXCEPCIONES

try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)
else:
    pass
finally:
    pass

# .
# El bloque else se ejecuta cuando todo lo del bloque ‘try’ se ejecuta correctamente, es decir, sin excepciones.
# .
# El bloque finally se ejcuta haya o no excepciones en el bloque ‘try’, es decir, que su ejecución es obligatoria

print('Hola')
print('Hola 2')