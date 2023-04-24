import tkinter as tk
from tkinter import messagebox

class banco:
    def __init__(self, caja):
        # Crear todo lo que va de la interfaz
        self.num_cuenta_label = tk.Label(caja, text="Número de cuenta:")
        self.num_cuenta_entry = tk.Entry(caja)
        self.titular_label = tk.Label(caja, text="Titular:")
        self.titular_entry = tk.Entry(caja)
        self.edad_label = tk.Label(caja, text="Edad:")
        self.edad_entry = tk.Entry(caja)
        self.saldo_label = tk.Label(caja, text="Saldo:")
        self.saldo_entry = tk.Entry(caja)
        self.consultar_saldo_button = tk.Button(caja, text="Consultar saldo", command=self.consultar_saldo)
        self.ingresar_label = tk.Label(caja, text="Cantidad a ingresar:")
        self.ingresar_entry = tk.Entry(caja)
        self.ingresar_button = tk.Button(caja, text="Ingresar efectivo", command=self.ingresar_efectivo)
        self.retirar_label = tk.Label(caja, text="Cantidad a retirar:")
        self.retirar_entry = tk.Entry(caja)
        self.retirar_button = tk.Button(caja, text="Retirar efectivo", command=self.retirar_efectivo)
        self.num_cuenta_dest_label = tk.Label(caja, text="Número de cuenta de destino:")
        self.num_cuenta_dest_entry = tk.Entry(caja)
        self.depositar_label = tk.Label(caja, text="Cantidad a depositar:")
        self.depositar_entry = tk.Entry(caja)
        self.depositar_button = tk.Button(caja, text="Depositar a otra cuenta", command=self.depositar_a_otra_cuenta)
        self.salir_button = tk.Button(caja, text="Salir", command=caja.quit)

        # Acomodar todo lo anterior en la interfaz
        self.num_cuenta_label.grid(row=0, column=0)
        self.num_cuenta_entry.grid(row=0, column=1)
        self.titular_label.grid(row=1, column=0)
        self.titular_entry.grid(row=1, column=1)
        self.edad_label.grid(row=2, column=0)
        self.edad_entry.grid(row=2, column=1)
        self.saldo_label.grid(row=3, column=0)
        self.saldo_entry.grid(row=3, column=1)
        self.consultar_saldo_button.grid(row=4, column=0)
        self.ingresar_label.grid(row=5, column=0)
        self.ingresar_entry.grid(row=5, column=1)
        self.ingresar_button.grid(row=6, column=0)
        self.retirar_label.grid(row=7, column=0)
        self.retirar_entry.grid(row=7, column=1)
        self.retirar_button.grid(row=8, column=1)
        self.num_cuenta_dest_label.grid(row=9, column=0)
        self.num_cuenta_dest_entry.grid(row=9, column=1)
        self.depositar_label.grid(row=10, column=0)
        self.depositar_entry.grid(row=10, column=1)
        self.depositar_button.grid(row=8, column=0)

    def consultar_saldo(self):
        # Obtener el número de cuenta
        num_cuenta = self.num_cuenta_entry.get()

        # Buscar la cuenta en la base de datos
        cuenta = self.buscar_cuenta(num_cuenta)

        # Actualizar los campos de la interfaz
        if cuenta is not None:
            self.titular_entry.delete(0, tk.END)
            self.edad_entry.delete(0, tk.END)
            self.saldo_entry.delete(0, tk.END)

            if "titular" in cuenta:
                self.titular_entry.insert(0, cuenta["titular"])
            if "edad" in cuenta:
                self.edad_entry.insert(0, cuenta["edad"])
            if "saldo" in cuenta:
                self.saldo_entry.insert(0, cuenta["saldo"])

    def ingresar_efectivo(self):
        # Obtener la cantidad a ingresar
        cantidad = float(self.ingresar_entry.get())

        # Obtener el número de cuenta
        num_cuenta = self.num_cuenta_entry.get()

        # Buscar la cuenta en la base de datos
        cuenta = self.buscar_cuenta(num_cuenta)

        # Verificar que la cuenta existe y la cantidad es positiva
        if cuenta is not None and cantidad > 0:
            # Actualizar el saldo de la cuenta
            cuenta["saldo"] += cantidad

            # Actualizar la entrada de saldo en la GUI
            self.saldo_entry.delete(0, tk.END)
            self.saldo_entry.insert(0, cuenta["saldo"])

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Se ha ingresado efectivo correctamente.")


    def retirar_efectivo(self):
        # Obtener la cantidad a retirar
        cantidad = float(self.retirar_entry.get())

        # Obtener el número de cuenta
        num_cuenta = self.num_cuenta_entry.get()

        # Buscar la cuenta en la base de datos
        cuenta = self.buscar_cuenta(num_cuenta)

        # Verificar que la cuenta existe, la cantidad es positiva y la cuenta tiene suficiente saldo
        if cuenta is not None and cantidad > 0 and cuenta["saldo"] >= cantidad:
            # Actualizar el saldo de la cuenta
            cuenta["saldo"] -= cantidad

            # Actualizar la entrada de saldo en la GUI
            self.saldo_entry.delete(0, tk.END)
            self.saldo_entry.insert(0, cuenta["saldo"])

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", f"Se ha retirado {cantidad} correctamente de la cuenta {num_cuenta}.")
        else:
            # Mostrar un mensaje de error si la cuenta no existe, la cantidad es negativa o la cuenta no tiene suficiente saldo
            messagebox.showerror("Error", "No se pudo retirar efectivo. Verifica que la cuenta existe, la cantidad es positiva y la cuenta tiene suficiente saldo.")



    def depositar_a_otra_cuenta(self):
        # Obtener el número de cuenta de destino y la cantidad a depositar
        num_cuenta_dest = self.num_cuenta_dest_entry.get()
        cantidad = float(self.depositar_entry.get())

        # Obtener el número de cuenta origen
        num_cuenta_origen = self.num_cuenta_entry.get()

        # Buscar las cuentas en la base de datos
        cuenta_origen = self.buscar_cuenta(num_cuenta_origen)
        cuenta_dest = self.buscar_cuenta(num_cuenta_dest)

        # Verificar que ambas cuentas existan y la cuenta origen tenga saldo suficiente
        if cuenta_origen is not None and cuenta_dest is not None and cuenta_origen["saldo"] >= cantidad:
            cuenta_origen["saldo"] -= cantidad
            cuenta_dest["saldo"] += cantidad
            tk.messagebox.showinfo("Éxito", f"Se depositó exitosamente {cantidad} a la cuenta de {num_cuenta_dest}")

            # Actualizar los campos de la interfaz
            self.saldo_entry.delete(0, tk.END)
            self.saldo_entry.insert(0, cuenta_origen["saldo"])
            self.num_cuenta_dest_entry.delete(0, tk.END)
            self.depositar_entry.delete(0, tk.END)

    def buscar_cuenta(self, num_cuenta):
        # Base de datos de cuentas
        cuentas = {
            "111": {"titular": "Miguel Quevedo", "edad": 21, "saldo": 5000},
            "222": {"titular": "Fortino", "edad": 20, "saldo": 4000},
            "333": {"titular": "Ricardo", "edad": 40, "saldo": 5000}
        }

        # Buscar la cuenta en la base de datos
        if num_cuenta in cuentas:
            return cuentas[num_cuenta]
        else:
            return None
ventana = tk.Tk()
app = banco(ventana)
ventana.mainloop()


