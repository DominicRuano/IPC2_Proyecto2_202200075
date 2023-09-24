
class SistemaDrones:
    def __init__(self,nombre,  Amax, Cdrones) -> None:
        self.nombre = nombre
        self.alturaMax = Amax
        self.cantidadDrones = Cdrones

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print(">>   Altura maxima: ", self.alturaMax, 
              "\n>>   Cantidad de drones: ", self.cantidadDrones)