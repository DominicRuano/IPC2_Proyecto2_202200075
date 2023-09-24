from graphviz import Graph
from dato import Dato

class lista_doble:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def insertar(self, dato):
        if self.primero is None:
            self.primero = Dato(dato)
            self.ultimo = self.primero
        else:
            actual = Dato(dato)
            self.ultimo.siguiente = actual
            self.ultimo = actual

    def recorrer(self):
        if self.primero is None:
            return
        actual = self.primero
        print(">>", actual.dato)
        while actual.siguiente:
            actual = actual.siguiente
            print(">>", actual.dato)

    def eliminar(self, usuario):
        actual = self.primero
        while actual:
            if actual.nota.usuario == usuario:
                if actual.anterior:
                    if actual.siguiente:
                        actual.anterior.siguiente = actual.siguiente
                        actual.siguiente.anterior = actual.anterior
                        actual.siguiente = None
                        actual.anterior = None
                    else:
                        actual.anterior.siguiente = None
                        actual.anterior = None
                else:
                    if actual.siguiente:
                        self.primero = actual.siguiente
                        actual.siguiente.anterior = None
                    else:
                        self.primero = None
                return True
            else:
                actual = actual.siguiente
        return False
        graph = Graph()
        tmp = self.DatoInicio
        while tmp:
            for a in range(self.size):
                if a == valor:
                    graph.addEncabezado(tmp)
                    graph.generar2(a)
                    return
                tmp = tmp.getSiguiente()