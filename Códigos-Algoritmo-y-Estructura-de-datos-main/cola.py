class Cola(object):
    
    def __init__(self):
        self.__elementos = []
    
    def arribo(self, dato):
        self.__elementos.append(dato)
    
    def atencion(self):
        return self.__elementos.pop(0)
    
    def cola_vacia(self):
        return len(self.__elementos) == 0
    
    def en_frente(self):
        return self.__elementos[0]
    
    def mover_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato
    
    def tamanio(self):
        return len(self.__elementos)