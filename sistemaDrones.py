from contenido import Contenido

class SistemaDrones:
    def __init__(self,nombre,  Amax, Cdrones, listaDatos) -> None:
        self.nombre = nombre
        self.alturaMax = Amax
        self.cantidadDrones = Cdrones
        self.datos = listaDatos  #[[drona, strLasLetras],[dronb, strLasLetras], ...]

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print(">>   Altura maxima: ", self.alturaMax, 
              "\n>>   Cantidad de drones: ", self.cantidadDrones)
        temp = self.datos.primero
        while temp:
            print(f">>      Nombre Del dron: {temp.getDato().NombreDron} | Letras: {temp.getDato().letrasSTR}")
            temp = temp.getSiguiente()