import xml.etree.ElementTree as ET
from ListaDoble import lista_doble
from sistemaDrones import SistemaDrones
from contenido import Contenido
from instruccion import Instruccion
from mensaje import Mensaje

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaDrones = lista_doble() #[nombre, nombre, ...]
        self.listaSistemas = lista_doble() #[[nombre, Amax, Cdrones, [[drona, strLasLetras],[dronb, strLasLetras], ...], ...]
        self.mensajes = lista_doble() #[[nombre, mensaje], ...]

    def getDrones(self) -> None:
        for a in self.root.findall("listaDrones"):
            for b in a.findall("dron"):
                if self.listaDrones.longitud <= 100:
                    self.listaDrones.insertar(b.text)
                else:
                    print(">> La cantidad de drones es mayor a 100")
                    return

    def getSistemas(self):
        for a in self.root.findall("listaSistemasDrones"):
            for b in a.findall("sistemaDrones"):
                lista = lista_doble()
                nombre = b.get("nombre")
                alturaMax = b.find("alturaMaxima").text
                cantidadDrones = b.find("cantidadDrones").text
                for c in b.findall("contenido"):
                    nombreDron = c.find("dron").text
                    letrasSTR = ""
                    for d in c.find("alturas").findall("altura"):
                        if len(letrasSTR) < int(alturaMax):
                            letrasSTR += d.text
                    temp = self.listaDrones.primero
                    valor = False
                    while temp:
                        if temp.dato == nombreDron:
                            valor = True
                            break
                        temp = temp.siguiente
                    if valor:
                        lista.insertar(Contenido(nombreDron, letrasSTR))
                    else:
                        print(f">> El dron {nombreDron} no existe")
                        continue
                self.listaSistemas.insertar(SistemaDrones(nombre, alturaMax, cantidadDrones, lista))

    def getMensajes(self):
        for a in self.root.findall("listaMensajes"):
            for b in a.findall("Mensaje"):
                lista = lista_doble()
                nombre = b.get("nombre")
                sistema = b.find("sistemaDrones").text
                for c in b.find("instrucciones").findall("instruccion"):
                    dron = c.get("dron")
                    dato = c.text
                    temp = self.listaDrones.primero
                    valor = False
                    while temp:
                        if temp.dato == dron:
                            valor = True
                            break
                        temp = temp.siguiente
                    if valor:
                        lista.insertar(Instruccion(dron, dato))
                    else:
                        print("una instruccion nombra un dron que no esta en la lista de drones, se saltara esta instruccion.")
                temp2 = self.listaSistemas.primero
                valor2 = False
                while temp2:
                    if temp2.getDato().nombre == sistema:
                        valor2 = True
                        break
                    temp2 = temp2.siguiente
                if valor2:
                    self.mensajes.insertar(Mensaje(nombre, sistema, lista))
                else:
                    print(f"el sistema de drones del mensaje, {nombre} no existe, por eso no se incluira.")

