from controlador import controlador
import tkinter as tk

def __init__(self, master):
    # Creamos un objeto de la clase controladorBD
    controlador = controlador()
    self.master = master
    self.master.title("Ferreteria")

    self.Material_label = tk.Label(master, text="Material: ")
    self.Material_label.grid(row=0, column=0)
    self.Material_entry = tk.Entry(master)
    self.Material_entry.grid(row=0, column=1)

    self.Cantidad_label = tk.Label(master, text="Cantidad:")
    self.Cantidad_label.grid(row=1, column=0)
    self.Cantidad_entry = tk.Entry(master)
    self.Cantidad_entry.grid(row=1, column=1)

    self.insertar_btn = tk.Button(master, text="Insertar", command=self.insertar)
    self.insertar_btn.grid(row=3, column=0)

    self.actualizar_btn = tk.Button(master, text="Actualizar", command=self.actualizar)
    self.actualizar_btn.grid(row=3, column=1)

    self.consultar_btn = tk.Button(master, text="Consultar", command=self.consultar)
    self.consultar_btn.grid(row=4, column=0)

    self.resultados_text = tk.Text(master, height=10, width=30)
    self.resultados_text.grid(row=5, columnspan=2)

root = tk.Tk()
root.mainloop()
