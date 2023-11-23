# 5
# Extender la siguiente clase e implementar la clase GrafoDirigidoPesado. 
# Utilizando la representación de matríz de adjacencia (deberán cambiar listaDeVertices por la matríz requerida).

class GrafoDirigidoPesado(Grafo):
    def __init__(self):
        super().__init__()
        self.lista_de_vertices = []
        self.matriz_adyacencia = {} 
        #se utiliza un diccionario ya que no requiere que se pase el numero de aristas al ser creado

    def conectar(self, vertice1, vertice2, peso):
        if vertice1 in self.lista_de_vertices and vertice2 in self.lista_de_vertices:
            self.matriz_adyacencia[vertice1][vertice2] = peso


#Considero que los demas metodos se mantienen igual, el metodo conectar es el que verdaderamente cambia  
#ya que suma el peso. Los demas cambian en el sentido de que se incorpora la matriz de adyacencia, pero serian igual en la clase Grafo y la clase GrafoDirigidoPesado, 
#los cuales asumo que ya tienen la matriz en predeterminado. 

#la otra forma de instanciar el grafo seria parecida a esta
from math import inf

class GrafoDirigidoPesado:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adyacencia = [[float('inf')] * num_vertices for _ in range(num_vertices)]

# 6
# Añadir a la clase GrafoDirigidoPesado un método conectividad() el cual retorna True si el grafo está furtemente conectado
    

    def conectividad(self):
        for vertice in self.lista_de_vertices:
            visitados = []
            self.dfs(vertice, visitados)
            
            if len(visitados) != len(self.lista_de_vertices): #si encuentra un solo vertice que no llegue a todos devuelve false
                return False 
        return True

    def dfs(self, vertice, visitados):
        visitados.append(vertice)
        for adyacente in self.matriz_adyacencia[vertice]:
            if adyacente not in visitados:
                self.dfs(adyacente, visitados)
                
    #Donde dfs sigue la logica de la bibliografia
    
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

#7
#Añadir a la clase GrafoDirigidoPesado un método ordenTopologico() el cual retornará una árbol binario de búsqueda con los vertices del grafo en orden descendente

#se reutiliza en metodo dfs
    def ordenTopologico(self):
        visitados = []
        orden_topologico = []
        
        for vertice in self.lista_de_vertices:
            if vertice not in visitados:
                self.dfs(vertice, visitados)

        nodos = list(reversed(orden_topologico))
        Arbol = ArbolBinarioBusqueda()
        for i in nodos:
            Arbol.insertar(i) 
        return Arbol

class ArbolBinarioBusqueda():
    def __init__(self):
        pass
    
#8
# Añadir a la clase GrafoDirigidoPesado un método caminoDijsktra() el cual retornará un camino minímo dentro del grafo. 
# Deben implementar el algoritmo de Dijkstra utilizando un montículo como estructura de datos suplementaria. 

# en este caso, me cuesta aplicar a la estructura que construi antes, a la bibliografia me remito
#donde el heap es una cola de proridad, y voy a hacer de cuenta que las importo

from math import inf
from heap import Heap
from pila import Pila

def dijkstra(grafo, origen, destino):
    """Devuelve el camino más corto desde el vértice 
    origen al vértice destino"""
    no_visitados = Heap(tamanio(grafo))
    camino = Pila()
    aux = grafo.inicio
    while (aux is not None):
        if (aux.info == origen):
            arribo_heap(no_visitados, [aux, None], 0)
        else:
            arribo_heap(no_visitados, [aux, None], inf)
        aux = aux.sig
        
    while (not heap_vacio(no_visitados)):
        dato = atencion_heap(no_visitados)
        apilar(camino, dato)
        aux = dato[1][0].adyacentes.inicio
        while (aux is not None):
            pos = buscar_heap(no_visitados, aux.destino)
            if (no_visitados.vector[pos][0] > dato[0] + aux.info):
                no_visitados.vector[pos][1][1] = dato[1][0].info
                cambiar_prioridad_heap(no_visitados, pos, dato[0] + aux.info)
            aux.sig
    return camino       



    





