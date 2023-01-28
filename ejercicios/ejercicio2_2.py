#funcion que retorne los numeros primos entre 0 y el argunmento

#funcion para validar que un numero sea primo
def is_prime(number):

    """
        se valida que el numero indicado no pueda dividirse
        por ningun numero entre 2 y el numero -1

        recibe como parametro number -> int => el numero a validar
        se retorna False si el numero tiene un divisor
        se retorna True si el numero no tiene divisores, 
        en ese caso es primo
    """
    for i in range(2, number - 1):
        if number % i == 0:
            return False

    return True

def primes_until(until):

    """
        utilizamos la funcion que valida si un numero es primo
        para validar cada primo que haya desde 2 hasta el numero indicado

        recibe como parametro until -> int => la distancia que recorreremos buscando numeros primos
        retorna primes que es una lista con todos los numeros primos encontrados
    """

    primes = []

    for i in range(3, until + 1):
        resultado = is_prime(i)

        if resultado == True:
            primes.append(i)

    return primes

result = primes_until(98)
print(result)