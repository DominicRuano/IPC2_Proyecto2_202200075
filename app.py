from XML import leerXML
import os


try:
    obj = leerXML("entradaV3.xml")
    os.system("cls")
    obj.getDrones()
    obj.getSistemas()
    obj.getMensajes()

    print("Lista de Drones")
    obj.listaDrones.recorrerDrones()
    print(f">>  El total de drones es: {obj.listaDrones.longitud}\n")

    print("Lista de Sistemas de Drones")
    temp = obj.listaSistemas.primero
    while temp:
        temp.getDato().imprimir()
        temp = temp.getSiguiente()

    print("\nLos mensajes son:")
    temp = obj.mensajes.primero
    while temp:
        print(f">>   Dron: {temp.getDato().nombre}\n>>   Sistema: {temp.getDato().sistema}\n>>   Las instrucciones son:")
        temp2 = temp.getDato().instrucciones.primero
        while temp2:
            print(f">>      {temp2.getDato().dron} | Dato: {temp2.getDato().dato}")
            temp2 = temp2.siguiente
        temp = temp.siguiente

except Exception as e:
    print(e)