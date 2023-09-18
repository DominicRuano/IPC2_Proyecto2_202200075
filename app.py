from XML import leerXML
import os


try:
    obj = leerXML("entradaV3.xml")
    os.system("cls")
    obj.getTodo()

    print("Lista de Drones")
    obj.listaDrones.imprimir()
    print("Lista de Sistemas de Drones")
    #aun no funciona

except Exception as e:
    print(e)