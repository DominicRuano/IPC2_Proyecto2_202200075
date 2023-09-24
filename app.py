from XML import leerXML
import os


try:
    obj = leerXML("entradaV3.xml")
    os.system("cls")
    obj.getTodo()

    print("Lista de Drones")
    obj.listaDrones.recorrer()
    print("Lista de Sistemas de Drones")
    temp = obj.listaSistemas.primero
    while temp:
        temp.getDato().imprimir()
        temp = temp.getSiguiente()

except Exception as e:
    print(e)