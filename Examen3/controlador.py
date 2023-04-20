
import sqlite3
from tkinter import messagebox
import tkinter
import tkinter as tk



class controlador:

    def __init__(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):

        try:
            conexion = sqlite3.connect("C:/Users/migue/OneDrive/Documentos/GitHubPOO/ProgramacionS181/Examen3/Ferreteria.db")
            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")
            
    def insertar(self):
        Material = self.Material_entry.get()
        Cantidad = self.Cantidad_entry.get()
        self.cursor.execute("INSERT INTO MatConstruccion VALUES (?, ?, ?)", (Material,Cantidad))
        self.conexion.commit()

    def actualizar(self):
        Material = self.Material_entry.get()
        Cantidad = self.Cantidad_entry.get()
        self.cursor.execute("UPDATE MatConstruccion SET Material=?, Cantidad=?", (Material,Cantidad))
        self.conexion.commit()

    def consultar(self):
        self.resultados_text.delete(1.0, tk.END)
        Material = self.Material_entry.get()
        self.cursor.execute("SELECT * FROM MatConstruccion WHERE Material=?", (Material))
        resultados = self.cursor.fetchall()
        for resultado in resultados:
            self.resultados_text.insert(tk.END, f"Material: {resultado[0]}\n")
            self.resultados_text.insert(tk.END, f"Cantidad: {resultado[1]}\n")
            