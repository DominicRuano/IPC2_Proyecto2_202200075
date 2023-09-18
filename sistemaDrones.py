
class SistemaDrones:
    def __init__(self,nombre,  Amax, Cdrones) -> None:
        self.nombre = nombre
        self.alturaMax = Amax
        self.cantidadDrones = Cdrones

    def imprimir(self):
        print("Altura maxima: ", self.alturaMax, "cantidad de drones: ", self.cantidadDrones)