from math import inf
import Heap

class nodoArista():
    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo():
    def __init__(self, dirigido = True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0
        
###############################
def tamanio(grafo):
    """Devuelve la cantidad de vértices en la grafo"""
    return grafo.tamanio

def grafo_vacio(grafo):
    """Devuelve verdadero (true) si el grafo no contiene elementos""" 
    return grafo.inicio is None

def buscar_vertice(grafo, buscado):
    """Devuelve un puntero que apunta al vértice que contiene un elemento que coincida con la clave (el primero que encuentra), 
    si devuelve None significa que no se encontró la clave en el grafo"""   
    aux = grafo.inicio
    while (aux is not None and aux.info != buscado):
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    """Devuelve un puntero que apunta a la arista 
    que contiene el elemento que coincida con el destino (el primero que encuentra), en la lista 
    de aristas del vértice origen, si devuelve None significa que no se encontró el destino desde el 
    vértice origen"""  
    aux = vertice.adyacentes.inicio
    while (aux is not None and aux.destino != buscado):
        aux = aux.sig
    return aux
        
def insertar_vertice(grafo, dato):
    """Agrega el elemento como un vértice al grafo""" 
    nodo = nodoVertice(dato)
    if (grafo.inicio is None or grafo.inicio.info > dato):
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while (act is not None and act.info < nodo.info):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio += 1

def insertar_arista(grafo, dato, origen, destino):
    """Agrega el elemento como una arista desde el vértice destino al vértice origen, si el grafo es dirigido 
    y si es no dirigido también lo inserta desde el vértice destino al origen"""
    agregar_arista(origen.adyacentes, dato, destino.info)
    if (not grafo.dirigido):
        agregar_arista(destino.adyacentes, dato, origen.info)

def agregar_arista(origen, dato, destino):   
    """Agrega una arista a la lista de aristas del 
    vértice origen al vértice destino"""
    nodo = nodoArista(dato, destino)
    if (origen.inicio is None or origen.inicio.destino > destino):
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while (act is not None and act.destino < nodo.destino):
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    """Elimina y devuelve del grafo si encuentra un vértice que coincida con la clave dada (el primero que encuentre) y 
    además recorre el resto de los vértices eliminando las aristas cuyo destino sea el vértice eliminado, 
    si devuelve None significa que no se encontró la clave en el grafo, y por ende no se elimina ningún elemento"""  
    x = None
    if (grafo.inicio.info == clave):
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while (act is not None and act.info != clave):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if (x is not None):
        aux = grafo.inicio
        while (aux is not None):
            if (aux.adyacentes.inicio is not None):
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x

def eliminar_arista(vertice, destino):
    """Elimina y devuelve del vértice si encuentra una arista que coincida con el destino dado (el primero que encuentre), 
    si devuelve None significa que no se encontró la arista destino en el vértice, y por ende no se elimina ningún elemento"""
    x = None
    if (vertice.inicio.destino == destino):
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while (act is not None and act.destino != destino):
            ant = act
            act = act.sig
        if (act is not None):
            x = act.info
            ant.sig = act.sig
            vertice.tamanio -= 1
    return x

def existe_paso(grafo, origen, destino):
    """Devuelve verdadero (true) si es posible ir desde el vértice origen hasta el vértice destino, caso contrario retornará falso (false)"""
    resultado = False
    if (not origen.visitado):
        origen.visitado = True
        vadyacentes = origen.adyacentes.inicio
        while (vadyacentes is not None and not resultado):
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if (adyacente.info == destino.info):
                return True
            elif (not adyacente.visitado):
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return True

def adyacentes(vertice): 
    """Realiza un barrido de los nodos adyacentes al vértice"""  
    aux = vertice.adyacentes.inicio
    while (aux is not None):
        print(aux.destino, aux.info)
        aux = aux.sig


def es_adyacente(vertice, destino):
    """Devuelve verdadero (true) si el destino es un nodo adyacente 
    al vértice"""
    resultado = False
    aux = vertice.adyacentes.inicio
    while (aux is not None and not resultado):
        if (aux.destino == resultado):
            resultado = True
        aux = aux.sig
    return resultado

def marcar_no_visitado(grafo):
    """ Marca todos los nodos vértices como no visitados poniendo el campo visitado con valor falso (false)"""
    aux = grafo.inicio
    while (aux is not None):
        aux.visitado = False
        aux = aux.sig
        
def barrido_vertices(grafo):
    """Realiza un barrido de los vértices ordenados"""
    aux = grafo.inicio
    while (aux is not None):
        print(aux.info)
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    """Realiza un barrido en profundidad del grafo a partir del vértice de inicio"""
    while (vertice is not None):
        if (not vertice.visitado):
            vertice.visitado = True
            print (vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while (adyacentes is not None):
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if (not adyacente.visitado):
                    barrido_profundidad(grafo, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
    """Realiza un barrido en amplitud del grafo a partir del 
    vértice de inicio"""
    cola = Cola()
    while (vertice is not None):
        if (not vertice.visitado):
            vertice.visitado = True
            arribo(cola, vertice)
            while (not cola_vacia(cola)):
                nodo = atencion(cola)
                print(nodo.info)
                adyacentes = nodo.adyacentes.inicio
                while (adyacentes is not None):
                    adyacente = buscar_vertice(grafo, adyacentes.destino)
                    if (not adyacente.visitado):
                        adyacente.visitado = True
                        arribo(cola, adyacente)
                    adyacentes = adyacentes.sig
        vertice = vertice.sig

def dijkstra(grafo, origen, destino):
    """Devuelve el camino más corto desde el vértice 
    origen al vértice destino"""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while (aux is not None):
        if (aux.info == origen):
            arribo_h(no_visitados, [aux, None], 0)
        else:
            arribo_h(no_visitados, [aux, None], inf)
        aux = aux.sig
        
    while (not heap_vacio(no_visitados)):
        dato = atencion_h(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while (aux is not None):
            pos = buscar_h(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad(no_visitados, pos, dato[0] + aux.info)
            aux.sig
    return camino       
    
    ##########################################################################################
class nodoPila():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Pila():
    def __init__(self):
        self.inicio = None

def apilar(pila, dato):
    """Agrega un elemento al final de la pila"""
    nodo = nodoPila(dato)
    if (pila.inicio is None):
        pila.inicio = nodo
    else:
        nodo.sig = pila.inicio
        pila.inicio = nodo

def desapilar(pila):
    """Devuelve el elemento del tope de la pila y lo elimina de la misma"""
    if (pila.inicio is None):
        return None
    else:
        dato = pila.inicio.info
        pila.inicio = pila.inicio.sig
        return dato

def pila_vacia(pila):
    """Devuelve verdadero (true) si la pila está vacía"""
    return pila.inicio is None
    
    ##########################################################################################     
class nodoCola():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Cola():
    def __init__(self):
        self.inicio = None
        self.fin = None

def arribo(cola, dato):
    """Agrega un elemento al final de la cola"""
    nodo = nodoCola(dato)
    if (cola.inicio is None):
        cola.inicio = nodo
    else:
        cola.fin.sig = nodo
    cola.fin = nodo

def atencion(cola):
    """Devuelve el elemento del frente de la cola y lo elimina de la misma"""
    if (cola.inicio is None):
        return None
    else:
        dato = cola.inicio.info
        cola.inicio = cola.inicio.sig
        if (cola.inicio is None):
            cola.fin = None
        return dato

def cola_vacia(cola):
    """Devuelve verdadero (true) si la cola está vacía"""
    return cola.inicio is None

    ##########################################################################################

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

def arribo_h(heap, dato, prioridad):
    agregar(heap, [prioridad, dato])
    
def atencion_h(heap):
    return quitar(heap)[1]

def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap[indice][0]
    heap[indice][0] = prioridad
    if (prioridad > prioridad_anterior):
        flotar(heap, indice)
    elif (prioridad < prioridad_anterior):
        hundir(heap, indice)

def buscar_h(heap, prioridad):
    for i in range(heap.tamanio):
        if heap.vector[i][0] == prioridad:
            return heap.vector[i][1]
    return None
