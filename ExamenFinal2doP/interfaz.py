import tkinter as tk
from logica import numRomano
from tkinter import messagebox

class numRomanoUI:
    def __init__(self, num):
        self.num = num
        self.num.title("Conversor de números romanos")
        self.convertidor = numRomano()

        self.ingresar_label = tk.Label(self.num, text="Ingrese número romano o arábigo (1-50): ")
        self.ingresar_label.pack()

        self.ingresar_entry = tk.Entry(self.num)
        self.ingresar_entry.pack()

        self.convert_boton = tk.Button(self.num, text="Convertir", command=self.convert)
        self.convert_boton.pack()

    def convert(self):
        ingresar_value = self.ingresar_entry.get()
        try:
            ingresar_value = int(ingresar_value)
            if ingresar_value > 50:
                raise ValueError("El número arábigo es mayor que 50")
            result = self.convertidor.romanoConvertido(ingresar_value)
        except ValueError:
            result = self.convertidor.arabigo(ingresar_value)

        if result is None:
            messagebox.showerror(title="Error", message=f"El número romano '{ingresar_value}' no existe.")
        else:
            messagebox.showinfo(title="Resultado", message=result)
