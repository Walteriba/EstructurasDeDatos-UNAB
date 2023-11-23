class HeapMax(object):
    
    def __init__(self):
        self.elementos = []
        self.tamanio = 0

    def vacio(self):
        return self.tamanio == 0

    def agregar(self, datos):
        self.elementos.append(datos)
        self.flotar(len(self.elementos)-1)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice-1) // 2
        while(indice > 0 and self.elementos[indice] > self.elementos[padre]):
            self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
            indice = padre
            padre = (indice-1) // 2
    
    def quitar(self):
        self.elementos[0], self.elementos[self.tamanio-1] = self.elementos[self.tamanio-1], self.elementos[0]
        self.tamanio -= 1
        self.hundir()
        return self.elementos[self.tamanio]

    def hundir(self, indice=0):
        hijo_izq = indice * 2 + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if(self.elementos[hijo_der] > self.elementos[hijo_izq]):
                    aux = hijo_der
            
            if(self.elementos[indice] < self.elementos[aux]):
                self.elementos[indice], self.elementos[aux] = self.elementos[aux], self.elementos[indice]
                indice = aux
                hijo_izq = indice * 2 + 1
            else:
                control = False

    def heap_sort(self):
        for i in range(self.tamanio):
            self.quitar()
    
    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()

    def monticulizar(self, datos):
        self.elementos = datos
        self.tamanio = len(datos)
        for i in range(self.tamanio):
            self.flotar(i)
    
    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterio = self.elementos[indice][0] 
        self.elementos[indice][0] = prioridad
        if(prioridad_anterio < prioridad):
            self.flotar(indice)
        else:
            self.hundir(indice)


class HeapMin(object):
    
    def __init__(self):
        self.elementos = []
        self.tamanio = 0

    def busqueda(self, buscado):
        for index in range(self.tamanio):
            if(self.elementos[index][1][0] == buscado):
                return index
    

    def vacio(self):
        return self.tamanio == 0


    def agregar(self, datos):
        self.elementos.append(datos)
        self.flotar(len(self.elementos)-1)
        self.tamanio += 1
    
    def flotar(self, indice):
        padre = (indice-1) // 2
        while(indice > 0 and self.elementos[indice] < self.elementos[padre]):
            self.elementos[indice], self.elementos[padre] = self.elementos[padre], self.elementos[indice]
            indice = padre
            padre = (indice-1) // 2
    
    def quitar(self):
        self.elementos[0], self.elementos[self.tamanio-1] = self.elementos[self.tamanio-1], self.elementos[0]
        self.tamanio -= 1
        self.hundir()
        dato = self.elementos[self.tamanio]
        self.elementos.pop()
        return dato

    def hundir(self, indice=0):
        hijo_izq = indice * 2 + 1
        control = True
        while(control and hijo_izq < self.tamanio):
            hijo_der = hijo_izq + 1
            aux = hijo_izq
            if(hijo_der < self.tamanio):
                if(self.elementos[hijo_der] < self.elementos[hijo_izq]):
                    aux = hijo_der
            
            if(self.elementos[indice] > self.elementos[aux]):
                self.elementos[indice], self.elementos[aux] = self.elementos[aux], self.elementos[indice]
                indice = aux
                hijo_izq = indice * 2 + 1
            else:
                control = False

    def heap_sort(self):
        for i in range(self.tamanio):
            self.quitar()

    def arribo(self, dato, prioridad):
        self.agregar([prioridad, dato])

    def atencion(self):
        return self.quitar()
    
    def monticulizar(self, datos):
        self.elementos = datos
        self.tamanio = len(datos)
        for i in range(self.tamanio):
            self.flotar(i)
    
    def cambiar_prioridad(self, indice, prioridad):
        prioridad_anterio = self.elementos[indice][0] 
        self.elementos[indice][0] = prioridad
        if(prioridad_anterio > prioridad):
            self.flotar(indice)
        else:
            self.hundir(indice)
