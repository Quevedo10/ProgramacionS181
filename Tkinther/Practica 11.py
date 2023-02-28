
from tkinter import Tk, Frame, Button

#Creación ventana

ventana = Tk()
ventana.title(" Practica 11: Frames ")
ventana.geometry("600x400")

#Definir secciones de la ventana
seccion1 = Frame(ventana, bg = "#cc0000")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg = "#ff9900")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana, bg = "#000000")
seccion3.pack(expand = True, fill = 'both') 

#Botones
botonAzul = Button(seccion1, text = "Botón Azul", bg = "#f2f2f2")
botonAzul.place(x=60, y=60)

botonAmarillo = Button(seccion2, text = "Botón Amarillo", bg = "#f2f2f2")
botonAmarillo.grid(row=0,column=0)

botonNegro = Button(seccion2, text = "Botón Negro", bg = "#f2f2f2")
botonNegro.grid(row=0,column=1)

botonblanco = Button(seccion3, text = "Botón blanco", bg = "#f2f2f2")
botonblanco.pack()

#Main de ejecución de ventana
ventana.mainloop()