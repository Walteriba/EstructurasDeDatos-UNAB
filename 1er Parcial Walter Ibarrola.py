# Pregunta 4
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self.agregarNodo(self.raiz, dato)

    def agregarNodo(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        
        if dato < nodo.dato:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self.agregarNodo(nodo.izq, dato)
        else:    
            if nodo.der is None:
                nodo.der = Nodo(dato)    
            else:
                self.agregarNodo(nodo.der, dato) 
        
        return nodo
    
    def buscar(self, dato):
        nodo = self.raiz
        while nodo is not None:
            if dato == nodo.dato:
                return nodo
            elif dato < nodo.dato:
                nodo = nodo.izq
            else:
                nodo = nodo.der

        raise ValueError("El elemento no se encontró")
    
    #Pregunta 6
    def imprimir_PreOrder(self):
        if self.raiz is None:
            print("Árbol vacío")
        else:
            self.preorden(self.raiz)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato)  
            self.preorden(nodo.izq)
            self.preorden(nodo.der)
    
    #Pregunta 7
    def imprimir_InOrder(self):
        if self.raiz is None:
            print("Árbol vacío")
        else:
            self.inorden(self.raiz)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izq)
            print(nodo.dato) 
            self.inorden(nodo.der)
    
    #Pregunta 7
    def imprimir_PostOrder(self): 
        """cambio un poco el metodo con respecto a los anteriores para 
            que imprima una lista"""
        if self.raiz is None:
            print("Árbol vacío")
        else:
            lista = []
            self.postorden(self.raiz, lista)
            print(lista)

    def postorden(self, nodo, lista):
        if nodo is not None:
            self.postorden(nodo.izq)
            self.postorden(nodo.der)
            lista.append(nodo.dato)
    
    def __str__(self):
        self.imprimir_PostOrder 


#Pregunta 5
class ArbolBinario_de_Busqueda(ArbolBinario):
    def __init__(self):
        super().__init__() 
    
    """
    Los metodos descritos para la clase Arbol Binario,
    ya cumplen con lo requerido para cumplir el hecho de agregar los nodos y
    sus respectivos datos en orden. Por lo tanto, se mantienen tal como estaban
    """      

