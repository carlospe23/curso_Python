# a(b) -> c

def my_custome_decorator(funcion_saludar): 

    def wrapper(*args, **kwargs):
        funcion_saludar(*args, **kwargs)
    
    return wrapper

@my_custome_decorator
def saludar(nombre):
    print(f'Hola {nombre}, como estas')


saludar('carlos')