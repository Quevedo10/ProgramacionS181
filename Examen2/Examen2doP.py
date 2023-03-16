from tkinter import messagebox
import tkinter as tk
import random

def generar_matricula():
        
    nombre = nombre.entry.get()
    apellidoPa = apellidoPa.entry.get()
    apellidoMa = apellidoMa.entry.get()
    año_nacimiento = año_nacimiento.entry.get()
    carrera = carrera.entry.get()

    letra_nombre = nombre[0]
    letra_apellidoPa = apellidoPa[2]
    letra_apellidoMa = apellidoMa[2]
    año_nacimiento = año_nacimiento[2]
    letra_carrera = carrera[3]
    aleat = str(random.randint(0, 99))[2]
    matricula = letra_nombre + letra_apellidoPa + letra_apellidoMa + año_nacimiento + letra_carrera + aleat
        
    matricula_label.config(text="Matrícula generada: " + matricula)

    ventana = tk.Tk()
    ventana.title("Generador de Matrículas UPQ")
    ventana.geometry("600x400")
    ventana.config(bg="white")

    nombre_label = tk.Label(ventana, text="Nombre: ")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana)
    nombre_entry.pack()

    apellidoPa_label = tk.Label(ventana, text="Apellido Paterno: ")
    apellidoPa_label.pack()
    apellidoPa_entry = tk.Entry(ventana)
    apellidoPa_entry.pack()

    apellidoMa_label = tk.Label(ventana, text="Apellido Materno: ")
    apellidoMa_label.pack()
    apellidoMa_entry = tk.Entry(ventana)
    apellidoMa_entry.pack()

    año_nacimiento_label = tk.Label(ventana, text="Año de Nacimiento: ")
    año_nacimiento_label.pack()
    año_nacimiento_entry = tk.Entry(ventana)
    año_nacimiento_entry.pack()

    carrera_label = tk.Label(ventana, text="Carrera: ")
    carrera_label.pack()
    carrera_entry = tk.Entry(ventana)
    carrera_entry.pack()

    generar_matricula_label = tk.Button(ventana, text="Aceptar", command = generar_matricula)
    generar_matricula_label.pack()

    matricula_label = tk.Label(ventana, text="")
    matricula_label.pack()

    messagebox.showinfo("Tu matricula es: " + matricula)

    ventana.mainloop()






        
