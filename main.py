import pickle
import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as MessageBox

listaContactos = []

def añadir():
    t = meterTel.get()
    n = meterNom.get()
    a = meterApe.get()
    listaContactos.append(t+"$"+n+"$"+a)
    excribirContacto()
    MessageBox.showinfo("Guardado", "Contacto guardado")
    meterTel.delete(0, "end")
    meterNom.delete(0, "end")
    meterApe.delete(0, "end")

def modificar():
    t = meterTel.get()
    n = meterNom.get()
    a = meterApe.get()
    for item in listaContactos:
        array = item.split("$")
        if meterTel.get() == array[0]:
            listaContactos.remove(item)
            listaContactos.append(t + "$" + n + "$" + a)
            excribirContacto()
            MessageBox.showinfo("Modificado", "Contacto Modificado")

    meterTel.delete(0, "end")
    meterNom.delete(0, "end")
    meterApe.delete(0, "end")

def borrar():
    t = entrarTel.get()
    eliminado = False
    for item in listaContactos:
        array = item.split("$")
        if entrarTel.get() == array[0]:
            listaContactos.remove(item)
            eliminado = True
    excribirContacto()
    if eliminado:
        MessageBox.showinfo("Eliminar", "Contacto eliminado")
    entrarTel.delete(0, "end")

def iniciarArchivo():
    archivo = open("contactos.txt", "a")
    archivo.close()

def cargar():
    archivo = open("contactos.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            listaContactos.append(linea)
            linea = archivo.readline()
    archivo.close()

def excribirContacto():
    archivo = open("contactos.txt", "w")
    listaContactos.sort()
    for item in listaContactos:
        archivo.write(item+"\n")
    archivo.close()

ventana = tk.Tk()
ventana.geometry("1130x600")
ventana.resizable(width=False, height=False)
ventana.configure(bg = "#212F3D")
ventana.title("Agenda Contactos")
fuente = tkFont.Font(family = "Syne Mono", size = 25)

iniciarArchivo()
cargar()

textoAgenda = tk.Label(ventana, text = "Agenda de Contactos", font = fuente, bg = "#212F3D", fg = "#3498DB")
textoAgenda.place(x=400, y=10)
textoTel = tk.Label(ventana, text = "Teléfono:", font = fuente, bg = "#212F3D", fg = "#3498DB")
textoTel.place(x = 30, y = 100)
textoNombre = tk.Label(ventana, text="Nombre:", font=fuente, bg = "#212F3D", fg = "#3498DB")
textoNombre.place(x = 30, y = 230)
textoApellidos = tk.Label(ventana, text="Apellidos:", font=fuente, bg = "#212F3D", fg = "#3498DB")
textoApellidos.place(x = 30, y = 360)
meterTel = tk.Entry(ventana, font=fuente, bg="#17202A", fg="#3498DB")
meterTel.place(x=220, y=100)
meterNom = tk.Entry(ventana, font=fuente, bg="#17202A", fg="#3498DB")
meterNom.place(x=220, y=230)
meterApe = tk.Entry(ventana, font=fuente, bg="#17202A", fg="#3498DB")
meterApe.place(x=220, y=360)
botonAñadir = tk.Button(ventana, text = "Añadir", font = fuente, bg = "#17202A", fg = "#3498DB", command = añadir)
botonAñadir.place(x=30, y=460)
botonModificar = tk.Button(ventana, text="Modificar", font=fuente, bg="#17202A", fg="#3498DB", command = modificar)
botonModificar.place(x=200, y=460)
textoTelBorrar = tk.Label(ventana, text="Tel:", font=fuente, bg = "#212F3D", fg = "#3498DB")
textoTelBorrar.place(x=620, y=100)
entrarTel = tk.Entry(ventana, textvariable= "elim", font=fuente, bg="#17202A", fg="#3498DB")
entrarTel.place(x=700, y=100)
botonBorrar = tk.Button(ventana, text="Borrar", font=fuente, bg="#17202A", fg="#3498DB", command = borrar)
botonBorrar.place(x=800, y=190)

ventana.mainloop()
