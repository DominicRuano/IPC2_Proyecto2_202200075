from XML import leerXML
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import os

# Constantes que definen el ancho y el alto de la ventana
WIDTH = 900  # Ancho
HEIGHT = 600 # Alto

obj = None

def Inicializar():
    global obj
    resultado = messagebox.askquestion("Inicializar el sistema", 
    "¿Está seguro que desea Inicializar el sistema?")

    if resultado == "yes":
        obj = None
        entry.config(state="normal")
        entry.delete(1.0, tk.END)
        entry.config(state="disabled")
        button6.place_forget()
        button1.config(state="normal")
        button.config(state="disabled")
        messagebox.showinfo("Sistema Inicializado", "Se inicializo en sistema.")


def cargarXML():
    button6.place_forget()
    try:
        path = filedialog.askopenfile(title="Seleccione el archivo",filetypes=(("XML files", ".xml"),("all files", ".*")))
        if path:
            global obj
            obj = leerXML(path)
            obj.getDrones()
            obj.getSistemas()
            obj.getMensajes()
            messagebox.showinfo("Cargar xml", "Se cargo correctamente el archivo.")
            button.config(state="normal")
            button1.config(state="disabled")
    except Exception as e:
        messagebox.showinfo("Error al cargar xml", f"Se produjo un error al cargar el archivo. \nError: {e}")

def generarXML():
    button6.place_forget()
    if obj != None:
        messagebox.showinfo("PENDIENTE", "ESTA FUNCION AUN NO FUNCIONA")
    else:
        messagebox.showerror("Error", "Aun no se ha cargado un archivo.")

def drones():
    global obj
    if obj:
        obj.ordenar()
        entry.config(state="normal")
        entry.delete(1.0, tk.END)
        texto = "> La lista de todos los drones es: \n\n"
        var = obj.listaDrones.primero
        while var:
            texto += f">>   {var.dato}\n"
            var = var.siguiente
        texto += f"\n> El total de drones es: {obj.listaDrones.longitud}"
        entry.insert(tk.END, texto)
        entry.config(state="disabled")
        button6.place(x=790, y=7, width=100, height=23)
    else:
        messagebox.showerror("Error", "Aun no se ha cargado un archivo.")

def adddron():
    global obj
    bool = True
    resultado = simpledialog.askstring("Agregar nuevo dron.", "Por favor, ingrese el nombre del nuevo dron (sin espacios en blanco):")
    temp = obj.listaDrones.primero
    if resultado == None:
        drones
        return
    while temp:
        if resultado.lower() == temp.dato.lower():
            bool = False
            messagebox.showerror("Error", "Ese dron ya existe, no se agregara.")
            break
        temp = temp.siguiente
    if bool and (resultado.count(" ") == 0) and resultado != "":
        obj.listaDrones.insertar(resultado)
        drones()

def sistemas():
    global obj
    if obj:
        filepath = "Sistemas.png"
        entry.config(state="normal")
        entry.delete(1.0, tk.END)
        entry.config(state="disabled")
        obj.graficarSistermas()
        os.system(f"start {filepath}")
        button6.place_forget()
    else:
        messagebox.showerror("Error", "Aun no se ha cargado un archivo.")

def mensajes():
    global obj
    if obj:
        obj.ordenarMensajes()
        button6.place_forget()
        mensaje = "> Los mensajes son:\n"
        temp = obj.mensajes.primero
        while temp:
            mensaje += f"\n>>   Mensaje: {temp.getDato().nombre}\n>>        Sistema de drones: {temp.getDato().sistema}\n>>        Instrucciones:\n"
            temp2 = temp.getDato().instrucciones.primero
            while temp2:
                mensaje += f">>           {temp2.getDato().dron} | Dato: {temp2.getDato().dato}\n"
                temp2 = temp2.siguiente
            temp = temp.siguiente
        mensaje += f"\n> Total de mensajes: {obj.mensajes.longitud}"
        entry.config(state="normal")
        entry.delete(1.0, tk.END)
        entry.insert(tk.END, mensaje)
        entry.config(state="disabled")
    else:
        messagebox.showerror("Error", "Aun no se ha cargado un archivo.")

def ayuda():
    mensaje = """
+--------------------------------------------------------------------------+
|                                                                          |
|   > Datos del estudiante:                                                |
|                                                                          |
|   >>  Dominic Juan Pablo Ruano Perez                                     |
|   >>  202200075                                                          |
|   >>  Introduccion a la Programacion y Computacion 2 seccion \"A\"         |
|   >>  Ingenieria en Ciencias y Sistemas                                  |
|   >>  4to semestre                                                       |
|                                                                          |
+--------------------------------------------------------------------------+
"""
    entry.config(state="normal")
    entry.delete(1.0, tk.END)
    entry.insert(tk.END, mensaje)
    entry.config(state="disabled")

# Creacion de la ventana
root = tk.Tk()
root.title("Seguridad en la Comunicación: Envío de Mensajes Encriptados")
root.resizable(False, False)
root.configure(bg="#444654")

# Centrar la ventana en la pantalla
ancho_pantalla = (root.winfo_screenwidth() - WIDTH) // 2 
alto_pantalla = (root.winfo_screenheight() - HEIGHT - 50) // 2 # 50 es la altura de la barra de tareas
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT,ancho_pantalla, alto_pantalla))

# Colorea el fondo de la ventana
label_fondo = tk.Label(root, background="#343541")
label_fondo.place(x=0, y=0, width=900, height=37)

# Crearcion de estilo para los combobox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= "#3E447D", background= "#3E447D", foreground= "white", bordercolor= "#343541", 
                arrowcolor= "white", borderwidth= 0.5, lightcolor= "white", darkcolor= "black")

# Creacion de los botones
button = tk.Button(root, text="Inicializar", bg="#333766", fg="white", borderwidth=0.5, command= lambda: Inicializar())
button1 = tk.Button(root, text="Cargar XML", bg="#333766", fg="white", borderwidth=0.5, command= lambda: cargarXML())
button2 = tk.Button(root, text="Generar XML", bg= "#333766", fg="white", borderwidth=0.5, command= lambda: generarXML())
button3 = tk.Button(root, text="Drones", bg="#333766", fg="white", borderwidth=0.5, command= lambda: drones())
button4 = tk.Button(root, text="Sistemas", bg="#333766", fg="white", borderwidth=0.5, command= lambda: sistemas())
button5 = tk.Button(root, text="Mensajes", bg="#333766", fg="white", borderwidth=0.5, command= lambda: mensajes())
button6 = tk.Button(root, text="Agregar Dron", bg="#333766", fg="white", borderwidth=0.5, command= lambda: adddron())
button7 = tk.Button(root, text="Ayuda", bg="#333766", fg="white", borderwidth=0.5, command= lambda: ayuda())


# Posicion de los botones
button.place(x=10, y=7, width=100, height=23)
button1.place(x=140, y=7, width=100, height=23)
button2.place(x=270, y=7, width=100, height=23)
button3.place(x=400, y=7, width=100, height=23)
button4.place(x=530, y=7, width=100, height=23)
button5.place(x=660, y=7, width=100, height=23)
button7.place(x=400, y=570, width=100, height=23)

# Creacion del tetxbox
entry = tk.Text(root, bg="#343541", fg="white", state="disabled")
entry.place(x=15, y=60, width=869, height=504)

button.config(state="disabled")

# Creacion de una etiqueda de advertencia
etiqueta = tk.Label(root, text="Esta ventana no se puede maximizar ni redimensionar.", bg="#444654", fg="white")
etiqueta.pack(padx=20, pady=37)

# Main
root.mainloop()