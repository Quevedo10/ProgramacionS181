import tkinter as tk
from logica import logica
from tkinter import messagebox

class logicaGUI:

    def __init__(self, interfaz):
        self.interfaz = interfaz
        interfaz.title("Conversiones")

        self.convertidor = logica()

        self.label = tk.Label(interfaz, text="Ingresa número Arabigo o Romano (1-50):")
        self.label.pack()

        self.entry = tk.Entry(interfaz)
        self.entry.pack()

        self.boton = tk.Button(interfaz, text="Convertir", command=self.convert)
        self.boton.pack()

    def convert(self):
        ingresar_value = self.entry.get()
        try:
            output_value = self.convertidor.convert(ingresar_value)
            tk.messagebox.showinfo("Resultado de la conversión: ", f"{ingresar_value} = {output_value}")
        except ValueError as e:
            tk.messagebox.showerror("Error de conversión", str(e))

ventana = tk.Tk()
gui = logicaGUI(ventana)
ventana.mainloop()
