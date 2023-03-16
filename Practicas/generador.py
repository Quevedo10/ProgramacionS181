import datetime
from tkinter import messagebox
import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        
        # Crear los widgets de la interfaz
        tk.Label(master, text="Nombre:").grid(row=0, column=0)
        tk.Label(master, text="Apellido paterno:").grid(row=1, column=0)
        tk.Label(master, text="Apellido materno:").grid(row=2, column=0)
        tk.Label(master, text="Año de nacimiento:").grid(row=3, column=0)
        tk.Label(master, text="Carrera:").grid(row=4, column=0)
        
        self.nombre_entry = tk.Entry(master)
        self.apellido_paterno_entry = tk.Entry(master)
        self.apellido_materno_entry = tk.Entry(master)
        self.year_nacimiento_entry = tk.Entry(master)
        self.carrera_entry = tk.Entry(master)
        
        self.nombre_entry.grid(row=0, column=1)
        self.apellido_paterno_entry.grid(row=1, column=1)
        self.apellido_materno_entry.grid(row=2, column=1)
        self.year_nacimiento_entry.grid(row=3, column=1)
        self.carrera_entry.grid(row=4, column=1)
        
        tk.Button(master, text="Generar matrícula", command=self.generar_matricula).grid(row=5, column=0, columnspan=2)
    
    def generar_matricula(self):
        nombre = self.nombre_entry.get()
        apellido_paterno = self.apellido_paterno_entry.get()
        apellido_materno = self.apellido_materno_entry.get()
        year_nacimiento = int(self.year_nacimiento_entry.get())
        carrera = self.carrera_entry.get()
        
        matricula = generar_matricula(nombre, apellido_paterno, apellido_materno, year_nacimiento, carrera
