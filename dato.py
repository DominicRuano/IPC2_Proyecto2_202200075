class Dato():
    def __init__(self, dato, anterior = None):
        self.dato = dato
        self.siguiente = None
        self.anterior = anterior

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self, anterior):
        self.anterior = anterior