from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill= 'both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)

#Pestaña1: Formulario de usuarios
titulo = Label(pestaña1, text='Registro de usuarios', fg='blue', font=('Modern',18)).pack()

varNom = tk.StringVar()
lblNom = Label(pestaña1, text="Nombre: ").pack()
txtNom = Entry(pestaña1, textvariable=varNom).pack()

varCor = tk.StringVar()
lblCor = Label(pestaña1, text="Correo: ").pack()
txtCor = Entry(pestaña1, textvariable=varCor).pack()

varCon = tk.StringVar()
lblCon = Label(pestaña1, text="Contraseña: ").pack()
txtCon = Entry(pestaña1, textvariable=varCon).pack()

btnGuardar = Button(pestaña1, text="Guardar Usuario")

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar usuario')

ventana.mainloop()