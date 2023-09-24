import xml.etree.ElementTree as ET
from ListaDoble import lista_doble
from sistemaDrones import SistemaDrones

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaDrones = lista_doble()
        self.listaSistemas = lista_doble()

    def getTodo(self) -> None:
        for a in self.root.findall("listaDrones"):
            for b in a.findall("dron"):
                self.listaDrones.insertar(b.text)
        
        for a in self.root.findall("listaSistemasDrones"):
            for b in a.findall("sistemaDrones"):
                nombre = b.get("nombre")
                alturaMax = b.find("alturaMaxima")
                cantidadDrones = b.find("cantidadDrones")
                self.listaSistemas.insertar(SistemaDrones(nombre, alturaMax.text, cantidadDrones.text))
    
    def graficar2(self, valor):
        pass

    def graficar3(self, valor):
        pass

    def generarArchivo(self):
        pass
