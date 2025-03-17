class Nodo:
    def __init__(self, valor):
        self.valor = valor 
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def vacio(self):
        return self.raiz is None   
     
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)
    def _buscar(self, nodo, valor): 
        if nodo is None:
            return None
        if valor == nodo.valor:
            return nodo
        if valor < nodo.valor:
            return self._buscar(nodo.izquierda, valor)
        else :
            return self._buscar(nodo.derecha, valor) 
         
    def insertar(self, valor):
        self.raiz = self._insertar(self.raiz, valor)
    def _insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        elif valor > nodo.valor:
            nodo.derecha = self._insertar(nodo.derecha, valor)
        return nodo
    
    def imprimir(self):
        self._imprimir(self.raiz)
    def _imprimir(self, nodo):
        if nodo is not None:
            
            self._imprimir(nodo.izquierda)
            
            self._imprimir(nodo.derecha)
            print(nodo.valor)

            
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

if __name__ == "__main__":
    main()                      