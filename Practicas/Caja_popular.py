
import tkinter as tk
from logica import *

class VentanaCuenta():
    def __init__(self, master, cuenta):
        self.cuenta = cuenta

        self.label_num_cuenta = tk.Label(master, text="No. Cuenta: " + cuenta.num_cuenta)
        self.label_titular = tk.Label(master, text="Titular: " + cuenta.titular)
        self.label_edad = tk.Label(master, text="Edad: " + str(cuenta.edad))
        self.label_saldo = tk.Label(master, text="Saldo: " + str(cuenta.saldo))

        self.button_consultar_saldo = tk.Button(master, text="Consultar saldo", command=self.consultar_saldo)
        self.button_ingresar_efectivo = tk.Button(master, text="Ingresar efectivo", command=self.ingresar_efectivo)
        self.button_retirar_efectivo = tk.Button(master, text="Retirar efectivo", command=self.retirar_efectivo)
        self.button_depositar_otra_cuenta = tk.Button(master, text="Depositar a otra cuenta", command=self.depositar_otra_cuenta)

        self.label_num_cuenta.pack()
        self.label_titular.pack()
        self.label_edad.pack()
        self.label_saldo.pack()
        self.button_consultar_saldo.pack()
        self.button_ingresar_efectivo.pack()
        self.button_retirar_efectivo.pack()
        self.button_depositar_otra_cuenta.pack()

    def consultar_saldo(self):
        saldo = self.cuenta.consultar_saldo()
        tk.messagebox.showinfo("Saldo", "El saldo de la cuenta es: " + str(saldo))
        self.label_saldo.config(text="Saldo: " + str(saldo))

    def ingresar_efectivo(self):
        cantidad = tk.simpledialog.askinteger("Ingresar efectivo", "Cantidad a ingresar:")
        if cantidad is not None:
            self.cuenta.ingresar_efectivo(cantidad)
            tk.messagebox.showinfo("Ingresar efectivo", "Se ha ingresado " + str(cantidad) + " pesos.")
            self.label_saldo.config(text="Saldo: " + str(self.cuenta.saldo))

    def retirar_efectivo(self):
        cantidad = tk.simpledialog.askinteger("Retirar efectivo", "Cantidad a retirar:")
        if cantidad is not None:
            self.cuenta.retirar_efectivo(cantidad)
            tk.messagebox
    def depositar_otra_cuenta(self):
        otra_cuenta = tk.simpledialog.askstring("Depositar a otra cuenta", "No. de cuenta a depositar:")
        cantidad = tk.simpledialog.askinteger("Depositar a otra cuenta", "Cantidad a depositar:")
        if otra_cuenta is not None and cantidad is not None:
            self.cuenta.depositar_otra_cuenta(otra_cuenta, cantidad)
            tk.messagebox.showinfo("Depositar a otra cuenta", "Se ha depositado " + str(cantidad) + " pesos en la cuenta " + otra_cuenta + ".")
            self.label_saldo.config(text="Saldo: " + str(self.cuenta.saldo))

        if __name__ == "__main__":
            cuentas = [
            Cuenta("001", "Juan Perez", 25, 1000),
            Cuenta("002", "Maria Gonzalez", 35, 500),
            Cuenta("003", "Pedro Ramirez", 45, 2000),
        ]

    root = tk.Tk()
    root.title("Caja Popular")

    frame_cuentas = tk.Frame(root)
    frame_cuentas.pack(side="left", padx=10, pady=10)

    root.mainloop()
