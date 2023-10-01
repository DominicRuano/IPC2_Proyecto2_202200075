import xml.etree.ElementTree as ET
from ListaDoble import lista_doble
from sistemaDrones import SistemaDrones
from contenido import Contenido
from instruccion import Instruccion
from mensaje import Mensaje
from graph import Graph

class leerXML:
    def __init__(self, path) -> None:
        self.root = ET.parse(path).getroot()
        self.listaDrones = lista_doble() #[nombre, nombre, ...]
        self.listaSistemas = lista_doble() #[[nombre, Amax, Cdrones, [[drona, strLasLetras],[dronb, strLasLetras], ...], ...]
        self.mensajes = lista_doble() #[[nombre, mensaje], ...]

    def getDrones(self) -> None:
        for a in self.root.findall("listaDrones"):
            for b in a.findall("dron"):
                if self.listaDrones.longitud <= 200:
                    self.listaDrones.insertar(b.text)
                else:
                    print(">> La cantidad de drones es mayor a 200, no se agregaran mas")
                    return

    def ordenar(self):
        for a in range(self.listaDrones.longitud):
            temp = self.listaDrones.primero
            while temp:
                if temp.anterior:
                    if temp.anterior.dato.lower() > temp.dato.lower():
                        temp.anterior.dato , temp.dato = temp.dato , temp.anterior.dato
                if temp.siguiente:
                    if temp.dato.lower() > temp.siguiente.dato.lower():
                        temp.siguiente.dato , temp.dato = temp.dato , temp.siguiente.dato
                temp = temp.siguiente

    def getSistemas(self):
        for a in self.root.findall("listaSistemasDrones"):
            for b in a.findall("sistemaDrones"):
                lista = lista_doble()
                nombre = b.get("nombre")
                alturaMax = b.find("alturaMaxima").text
                cantidadDrones = b.find("cantidadDrones").text
                for c in b.findall("contenido"):
                    nombreDron = c.find("dron").text
                    letrasSTR = lista_doble()
                    for d in c.find("alturas").findall("altura"):
                        if letrasSTR.longitud < int(alturaMax):
                            letrasSTR.insertar(d.text)
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
                if int(alturaMax) > 100:
                    print("La latura maxima es mayor a 100 por lo tanto no se tomaran en cuenta las alturas mayores y se tomara como maxima 100.")
                    self.listaSistemas.insertar(SistemaDrones(nombre, "100", cantidadDrones, lista))
                else:
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

    def graficarSistermas(self):
        contador = 1
        graph = Graph()
        sistemas = self.listaSistemas.primero
        graph.addEncabezado("Sistemas", contador)
        encabezado = contador
        contador += 1
        while sistemas:
            graph.add1Nodo(sistemas.dato.nombre, encabezado, contador) # nombre del sistema
            graph.add1Nodo(f"Amax:{sistemas.dato.alturaMax}", contador, contador + 1) # Amax
            graph.add1Nodo(f"Drones: {sistemas.dato.cantidadDrones}", contador, contador + 2)
            dato = sistemas.dato.datos.primero
            encabezado2 = contador
            contador = contador + 3
            graph.add1Nodo("Altura/Dron", encabezado2, contador)
            for a in range(int(sistemas.dato.alturaMax)):
                graph.add1Nodo(f"Altura: {a + 1}",contador, contador + 1)
                contador += 1
            contador += 1
            while dato:
                graph.add1Nodo(f"{dato.dato.NombreDron}", encabezado2, contador)
                linea = dato.dato.letrasSTR.primero
                while linea:
                    graph.add1Nodo(linea.dato, contador, contador + 1)
                    contador += 1
                    linea = linea.siguiente
                dato =  dato.siguiente
                contador += 1
            contador += 100000
            sistemas = sistemas.siguiente
        graph.graficar()
