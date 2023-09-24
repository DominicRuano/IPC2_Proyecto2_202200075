from XML import leerXML
import os


try:
    obj = leerXML("entradaV3.xml")
    os.system("cls")
    obj.getDrones()
    obj.getSistemas()

    print("Lista de Drones")
    obj.listaDrones.recorrerDrones()
    print(f">>  El total de drones es: {obj.listaDrones.longitud}\n")

    print("Lista de Sistemas de Drones")
    temp = obj.listaSistemas.primero
    while temp:
        temp.getDato().imprimir()
        temp = temp.getSiguiente()

except Exception as e:
    print(e)