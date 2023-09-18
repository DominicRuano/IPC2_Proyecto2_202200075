import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from sistemaDrones import SistemaDrones

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaDrones = ListaSimple()
        self.listaSistemas = ListaSimple()

    def getTodo(self) -> None:
        for a in self.root.findall("listaDrones"):
            for b in a.findall("dron"):
                self.listaDrones.agregarFinal(b.text)
        
        for a in self.root.findall("listaSistemasDrones"):
            for b in a.findall("sistemaDrones"):
                nombre = b.get("nombre")
                alturaMax = b.find("alturaMaxima")
                cantidadDrones = b.find("cantidadDrones")
                self.listaSistemas.agregarFinal(SistemaDrones(nombre, alturaMax.text, cantidadDrones.text))
    
    def graficar2(self, valor):
        pass

    def graficar3(self, valor):
        pass

    def generarArchivo(self):
        pass
