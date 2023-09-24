from graphviz import Graph
from dato import Dato

class lista_doble:
    def __init__(self) -> None:
        self.longitud = 0
        self.primero = None
        self.ultimo = None

    def insertar(self, dato):
        if self.primero is None:
            self.primero = Dato(dato)
            self.ultimo = self.primero
            self.longitud += 1
        else:
            actual = Dato(dato)
            self.ultimo.siguiente = actual
            self.ultimo = actual
            self.longitud += 1

    def recorrer(self):
        if self.primero is None:
            return
        actual = self.primero
        print(actual.dato)
        while actual.siguiente:
            actual = actual.siguiente
            print(actual.dato)

    def recorrerDrones(self):
        if self.primero is None:
            return
        actual = self.primero
        contador = 0
        print(">>   ", actual.dato)
        while actual.siguiente and contador < 101:
            actual = actual.siguiente
            print(">>   ", actual.dato)
            contador += 1

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
        return