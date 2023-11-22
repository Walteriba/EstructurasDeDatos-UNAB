class MonticuloMinimo:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.cantidad = 0
        self.heap = [None] * capacidad_maxima

    def obtener_padre(self, indice):
        return (indice - 1) // 2

    def obtener_hijo_izquierdo(self, indice):
        return 2 * indice + 1

    def obtener_hijo_derecho(self, indice):
        return 2 * indice + 2

    def intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def agregar(self, valor):
        if self.cantidad == self.capacidad_maxima:
            print("Montículo lleno. No se puede agregar más elementos.")
            return

        self.heap[self.cantidad] = valor
        self.flotar(self.cantidad)
        self.cantidad += 1

    def quitar(self):
        if self.cantidad == 0:
            print("Montículo vacío. No se puede quitar ningún elemento.")
            return None

        minimo = self.heap[0]
        self.cantidad -= 1
        self.heap[0] = self.heap[self.cantidad]
        self.heap[self.cantidad] = None
        self.hundir(0)

        return minimo

    def cantidad_elementos(self):
        return self.cantidad

    def vacio(self):
        return self.cantidad == 0

    def lleno(self):
        return self.cantidad == self.capacidad_maxima

    def flotar(self, indice):
        while indice > 0:
            indice_padre = self.obtener_padre(indice)
            if self.heap[indice] < self.heap[indice_padre]:
                self.intercambiar(indice, indice_padre)
                indice = indice_padre
            else:
                break

    def hundir(self, indice):
        while True:
            indice_izquierdo = self.obtener_hijo_izquierdo(indice)
            indice_derecho = self.obtener_hijo_derecho(indice)
            indice_menor = indice

            if (indice_izquierdo < self.cantidad and
                    self.heap[indice_izquierdo] < self.heap[indice_menor]):
                indice_menor = indice_izquierdo

            if (indice_derecho < self.cantidad and
                    self.heap[indice_derecho] < self.heap[indice_menor]):
                indice_menor = indice_derecho

            if indice_menor != indice:
                self.intercambiar(indice, indice_menor)
                indice = indice_menor
            else:
                break

# Ejemplo de uso:
capacidad_maxima = 10
monticulo = MonticuloMinimo(capacidad_maxima)
valores = [4, 8, 2, 6, 10, 1]

for valor in valores:
    monticulo.agregar(valor)

print("Montículo después de agregar valores:", monticulo.heap)

minimo = monticulo.quitar()
print("Valor mínimo extraído:", minimo)
print("Montículo después de quitar mínimo:", monticulo.heap)

print("Cantidad de elementos en el montículo:", monticulo.cantidad_elementos())
print("¿El montículo está vacío?", monticulo.vacio())
print("¿El montículo está lleno?", monticulo.lleno())

##################################################################################################################################################################

class Heap():
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

def agregar(heap, dato):
    """Inserta un elemento al final del montículo y luego lo flota hasta que 
    dicho elemento cumpla la propiedad de orden"""
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1
    
def quitar(heap):
    """Quita y devuelve el máximo o mínimo elemento del montículo (dependiendo de su tipo), 
    es decir el dato que se ubica en la raíz del árbol , y en su lugar se coloca 
    el último elemento del montículo y luego lo hunde hasta que cumpla la propiedad de orden"""
    intercambio(heap.vector[heap.tamanio - 1])
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato

def heap_vacio(heap):
    """Devuelve True si esta lleno"""
    return heap.tamanio == 0

def heap_lleno(heap):
    """Devuelve True si esta lleno"""
    return heap.tamanio == len(heap.vector)

def flotar(heap, indice):
    """Flota el dato almacenado en el montículo desde el índice indicado 
    hasta que cumpla la propiedad de orden"""
    while (indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]):
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre
        
def hundir(heap, indice):
    """Hunde el dato almacenado en el montículo desde el índice indicado 
    hasta que cumpla la propiedad de orden"""
    hijo_izq = (indice * 2) + 1
    control = True
    while (control and hijo_izq < heap.tamanio):
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if (hijo_der < heap.tamanio):
            if (heap.vector[hijo_der] > heap.vector[hijo_izq]):
                aux = hijo_der
        
        if (heap.vector[indice] < heap.vector[aux]):
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False
            
def intercambio(vector, indice1, indice2):
    aux = vector[indice1]
    vector[indice1] = vector[indice2]
    vector[indice2] = aux


def monticulizar(heap):
    """Transforma un vector en un monticulo"""
    for i in range(len(heap.vector)):
        flotar(heap, i)
    
# colas de prioridad

def arribo(heap, dato, prioridad):
    agregar(heap, [prioridad, dato])
    
def atencion(heap):
    return quitar(heap)[1]

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap[indice][0]
    heap[indice][0] = prioridad
    if (prioridad > prioridad_anterior):
        flotar(heap, indice)
    elif (prioridad < prioridad_anterior):
        hundir(heap, indice)
    

                