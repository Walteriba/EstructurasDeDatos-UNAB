# """
# Árbol AVL - Implementación en Python
# """

# from __future__ import print_function

# """
# Declaramos la clase "Node", con cada una de sus propiedades.
# """
# class Node:
#     def __init__(self, label):
#         self.label = label
#         self._parent = None
#         self._left = None
#         self._right = None
#         self.height = 0

#     @property
#     def right(self):
#         return self._right

#     @right.setter
#     def right(self, node):
#         if node is not None:
#             node._parent = self
#             self._right = node

#     @property
#     def left(self):
#         return self._left

#     @left.setter
#     def left(self, node):
#         if node is not None:
#             node._parent = self
#             self._left = node

#     @property
#     def parent(self):
#         return self._parent

#     @parent.setter
#     def parent(self, node):
#         if node is not None:
#             self._parent = node
#             self.height = self.parent.height + 1
#         else:
#             self.height = 0

# # Declaramos la clase AVL
# class AVL:

#     def __init__(self):
#         self.root = None
#         self.size = 0

#         """
#         Operación de inserción para agregar nuevos nodos
#         al árbol.
#         """
#     def insert(self, value):
#         node = Node(value)

#         if self.root is None:
#             self.root = node
#             self.root.height = 0
#             self.size = 1
#         else:
#             dad_node = None
#             curr_node = self.root

#             while True:
#                 if curr_node is not None:

#                     dad_node = curr_node

#                     if node.label < curr_node.label:
#                         curr_node = curr_node.left
#                     else:
#                         curr_node = curr_node.right
#                 else:
#                     node.height = dad_node.height
#                     dad_node.height += 1
#                     if node.label < dad_node.label:
#                         dad_node.left = node
#                     else:
#                         dad_node.right = node
#                     self.rebalance(node)
#                     self.size += 1
#                     break

#         # Operación de rotación
#     def rebalance(self, node):
#         n = node

#         while n is not None:
#             height_right = n.height
#             height_left = n.height

#             if n.right is not None:
#                 height_right = n.right.height

#             if n.left is not None:
#                 height_left = n.left.height

#             if abs(height_left - height_right) > 1:
#                 if height_left > height_right:
#                     left_child = n.left
#                     if left_child is not None:
#                         h_right = (left_child.right.height
#                                     if (left_child.right is not None) else 0)
#                         h_left = (left_child.left.height
#                                     if (left_child.left is not None) else 0)
#                     if (h_left > h_right):
#                         self.rotate_left(n)
#                         break
#                     else:
#                         self.double_rotate_right(n)
#                         break
#                 else:
#                     right_child = n.right
#                     if right_child is not None:
#                         h_right = (right_child.right.height
#                             if (right_child.right is not None) else 0)
#                         h_left = (right_child.left.height
#                             if (right_child.left is not None) else 0)
#                     if (h_left > h_right):
#                         self.double_rotate_left(n)
#                         break
#                     else:
#                         self.rotate_right(n)
#                         break
#             n = n.parent

#     def rotate_left(self, node):
#         aux = node.parent.label
#         node.parent.label = node.label
#         node.parent.right = Node(aux)
#         node.parent.right.height = node.parent.height + 1
#         node.parent.left = node.right


#     def rotate_right(self, node):
#         aux = node.parent.label
#         node.parent.label = node.label
#         node.parent.left = Node(aux)
#         node.parent.left.height = node.parent.height + 1
#         node.parent.right = node.right

#     def double_rotate_left(self, node):
#         self.rotate_right(node.getRight().getRight())
#         self.rotate_left(node)

#     def double_rotate_right(self, node):
#         self.rotate_left(node.getLeft().getLeft())
#         self.rotate_right(node)

#     def empty(self):
#         if self.root is None:
#             return True
#         return False

#     def preShow(self, curr_node):
#         if curr_node is not None:
#             self.preShow(curr_node.left)
#             print(curr_node.label, end=" ")
#             self.preShow(curr_node.right)

#     def preorder(self, curr_node):
#         if curr_node is not None:
#             self.preShow(curr_node.left)
#             self.preShow(curr_node.right)
#             print(curr_node.label, end=" ")

#     def getRoot(self):
#         return self.root

# if __name__ == '__main__':
#     t = AVL()
#     t.insert(5)
#     t.insert(9)
#     t.insert(13)
#     t.insert(10)
#     t.insert(17)
#     t.preShow(t.root)
    
#################################################################################################################################################################

class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1
        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1

        return x

    def rotar_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = max(self.altura(x.izquierda), self.altura(x.derecha)) + 1
        y.altura = max(self.altura(y.izquierda), self.altura(y.derecha)) + 1

        return y

    def rotar_simple(self, raiz, izquierda):
        if izquierda:
            y = raiz.izquierda
            raiz.izquierda = y.derecha
            y.derecha = raiz
        else:
            y = raiz.derecha
            raiz.derecha = y.izquierda
            y.izquierda = raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def rotar_doble(self, raiz, izquierda):
        if izquierda:
            raiz.izquierda = self.rotar_simple(raiz.izquierda, False)
            return self.rotar_simple(raiz, True)
        else:
            raiz.derecha = self.rotar_simple(raiz.derecha, True)
            return self.rotar_simple(raiz, False)

    def insertar(self, raiz, clave):
        if not raiz:
            return NodoAVL(clave)

        if clave < raiz.clave:
            raiz.izquierda = self.insertar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self.insertar(raiz.derecha, clave)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))

        balance = self.balance(raiz)

        # Caso izquierda-izquierda
        if balance > 1 and clave < raiz.izquierda.clave:
            return self.rotar_derecha(raiz)

        # Caso derecha-derecha
        if balance < -1 and clave > raiz.derecha.clave:
            return self.rotar_izquierda(raiz)

        # Caso izquierda-derecha
        if balance > 1 and clave > raiz.izquierda.clave:
            return self.rotar_doble(raiz, True)

        # Caso derecha-izquierda
        if balance < -1 and clave < raiz.derecha.clave:
            return self.rotar_doble(raiz, False)

        return raiz

    def insertar_clave(self, clave):
        self.raiz = self.insertar(self.raiz, clave)

    def eliminar(self, raiz, clave):
        if not raiz:
            return raiz

        if clave < raiz.clave:
            raiz.izquierda = self.eliminar(raiz.izquierda, clave)
        elif clave > raiz.clave:
            raiz.derecha = self.eliminar(raiz.derecha, clave)
        else:
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            temp = self.min_valor_nodo(raiz.derecha)
            raiz.clave = temp.clave
            raiz.derecha = self.eliminar(raiz.derecha, temp.clave)

        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))

        balance = self.balance(raiz)

        # Rebalancear el árbol

        # Caso izquierda-izquierda
        if balance > 1 and self.balance(raiz.izquierda) >= 0:
            return self.rotar_derecha(raiz)

        # Caso izquierda-derecha
        if balance > 1 and self.balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotar_izquierda(raiz.izquierda)
            return self.rotar_derecha(raiz)

        # Caso derecha-derecha
        if balance < -1 and self.balance(raiz.derecha) <= 0:
            return self.rotar_izquierda(raiz)

        # Caso derecha-izquierda
        if balance < -1 and self.balance(raiz.derecha) > 0:
            raiz.derecha = self.rotar_derecha(raiz.derecha)
            return self.rotar_izquierda(raiz)

        return raiz

    def eliminar_clave(self, clave):
        self.raiz = self.eliminar(self.raiz, clave)

    def min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
