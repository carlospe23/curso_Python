import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 10000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo_r = time.time()
    factorial_r(n)
    final_r = time.time()
    print(final_r - comienzo_r)