import tkinter as tk
from tkinter import messagebox
from generadorContra import generadorContra


class Contrasena:
    def __init__(self):
        self._generador = generadorContra()
        self._ventana = tk.Tk()
        self._ventana.title("Generador de Contraseña")

        self._longitud_label = tk.Label(self._ventana, text="Cantidad de caracteres:", font=("Arial", 12), fg="white", bg="gray")
        self._longitud_label.grid(row=0, column=0, padx=10, pady=10)

        self._longitud_var = tk.StringVar()
        self._longitud_var.set("8")
        self._longitud_entry = tk.Entry(self._ventana, textvariable=self._longitud_var, font=("Arial", 12), width=10)
        self._longitud_entry.grid(row=0, column=1)

        self._mayusculas_var = tk.BooleanVar()
        self._mayusculas_var.set(True)
        self._mayusculas_checkbox = tk.Checkbutton(
            self._ventana,
            text="Incluir Mayusculas",
            variable=self._mayusculas_var,
            font=("Arial", 12),
            fg="black",
            bg="gray"
        )
        self._mayusculas_checkbox.grid(row=1, column=0)

        self._caracteres_var = tk.BooleanVar()
        self._caracteres_var.set(True)
        self._caracteres_checkbox = tk.Checkbutton(
            self._ventana,
            text="Incluir Caracteres",
            variable=self._caracteres_var,
            font=("Arial", 12),
            fg="black",
            bg="gray"
        )
        self._caracteres_checkbox.grid(row=2, column=0)

        self._boton = tk.Button(self._ventana, text="Generar contraseña", command=self.contrasenaGenerada, font=("Arial", 12), fg="white", bg="gray")
        self._boton.grid(row=3, column=0, columnspan=2, pady=10)

        self._contrasena_label = tk.Label(self._ventana, text="Contraseña: ", font=("Arial", 12), fg="white", bg="gray")
        self._contrasena_label.grid(row=4, column=0, padx=10, pady=10)

        self._contrasena_textbox = tk.Text(self._ventana, height=1, font=("Arial", 12), width=20)
        self._contrasena_textbox.grid(row=4, column=1)

        self._ventana.configure(bg="gray")
        self._ventana.mainloop()

    def contrasenaGenerada(self):
        self._generador.set_longitud(int(self._longitud_var.get()))
        self._generador.mayusculas(self._mayusculas_var.get())
        self._generador.caracteres(self._caracteres_var.get())
        contra = self._generador.contrasenaGenerada()
        self._contrasena_textbox.delete(1.0, tk.END)
        self._contrasena_textbox.insert(tk.END, contra)
        messagebox.showinfo("Contraseña generada", contra)


if __name__ == "__main__":
    app = Contrasena()


