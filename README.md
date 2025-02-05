Arbol binario de busqueda
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
__init__: Este es el constructor de la clase Nodo.
self.valor: Almacena el valor del nodo.
self.izquierda: Hace referencia al nodo hijo izquierdo, el cual inicialmente es None.
self.derecha: Hace referencia al nodo hijo derecho, el cual inicialmente es None como el izquierdo.

class Arbol:
    def __init__(self):
        self.raiz = None
__init__: Este es el constructor de la clase Arbol.
self.raiz: Hace referencia a la raíz del árbol. Inicialmente es None, por lo que el arbol esta vacio.

def vacio(self):
    return self.raiz is None
vacio: Este método verifica si el árbol está vacío.
self.raiz is None: Retorna True si la raíz es None, nos indica que el árbol está vacío. De lo contrario, retorna False.

def buscar(self, valor):
    return self._buscar(self.raiz, valor)
buscar: Este método busca un valor en el árbol.
self._buscar(self.raiz, valor): Llama al método privado _buscar pasando la raíz del árbol y el valor a buscar.

def _buscar(self, nodo, valor):
    if nodo is None:
        return None
    if valor == nodo.valor:
        return nodo
    if valor < nodo.valor:
        return self._buscar(nodo.izquierda, valor)
    else:
        return self._buscar(nodo.derecha, valor)
_buscar: Este método realiza la búsqueda recursiva de un valor en el árbol.
if nodo is None: Si el nodo actual es None, el valor no se encuentra en el árbol y devuelve None.
if valor == nodo.valor: Si el valor del nodo actual es igual al valor buscado, devuelve el nodo actual.
if valor < nodo.valor: Si el valor buscado es menor que el valor del nodo actual, busca en el subárbol izquierdo.
else: Si el valor buscado es mayor que el valor del nodo actual, busca en el subárbol derecho.

def imprimir(self):
    self._imprimir(self.raiz)
imprimir: Este método público se utiliza para iniciar el proceso de impresión del árbol.
self._imprimir(self.raiz): Llama al método privado _imprimir pasando la raíz del árbol. Esto inicia la impresión desde la raíz.

def _imprimir(self, nodo):
    if nodo is not None:
        print(nodo.valor)
        self._imprimir(nodo.izquierda)
        self._imprimir(nodo.derecha)
_imprimir: Este método privado realiza la impresión recursiva de los valores del árbol en preorden (raíz, izquierda, derecha).
if nodo is not None: Verifica si el nodo actual no es None. Si es None, significa que se ha alcanzado una hoja y no hay más nodos que imprimir en esta rama.
print(nodo.valor): Imprime el valor del nodo actual.
self._imprimir(nodo.izquierda): Llama recursivamente al método _imprimir para imprimir el subárbol izquierdo.
self._imprimir(nodo.derecha): Llama recursivamente al método _imprimir para imprimir el subárbol derecho.

def main():
    a = Arbol()
    print("esta mi arbol vacio?", a.vacio())
    a.insertar(5)
    a.insertar(3)
    a.insertar(7)
    a.insertar(2)
    a.insertar(4)
    a.insertar(6)
    a.insertar(8)
    a.imprimir()
    print(a.buscar(2).valor)
    print("esta mi arbol vacio?", a.vacio())
a.imprimir(): Llama al método imprimir del árbol a, lo que inicia el proceso de impresión del árbol.
 
