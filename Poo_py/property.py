class Empleado:
    
    def __init__(self, nombre, clave = None):
        self.nombre = nombre
        self.__clave = clave

    @property
    def key(self):
        return self.__clave

    
    @key.setter
    def key(self, value):
        self.__clave = value

    

em = Empleado(nombre = 'juan', clave = 'asdasd')

print(em.key)