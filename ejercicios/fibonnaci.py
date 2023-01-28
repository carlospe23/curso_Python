# sucession de fibonnaci hasta el numero indicado

def fibonacci(n):

    """
        encuentra la secuencia fibonnaci hasta el numero n

        recibe como parametro n -> int 
        n sera el punto hasta el cual queremos encontrar
        la secuencia

        retorna unas estructura recursiva de la misma funcion 
        pero con la formula que nos permitira encontrar fibonnaci
    """

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('digite un numero: '))

print(fibonacci(n))

def fibonnaci_2(number):
    a, b = 0, 1
    fibonacci_list = [0]

    for _ in range(number):

        if b > number: 
            return fibonacci_list
        else:
            fibonacci_list.append(b)
            a, b = b, a + b

    return fibonacci_list

resultado = fibonacci(20)
print(resultado)

