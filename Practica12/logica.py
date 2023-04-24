import tkinter as tk
import tkinter.messagebox as messagebox

class login:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Login")
        self.parent.geometry("500x300")
        self.parent.resizable(False, False)
        self.parent.config(bg="#7EBDC2")
        
        self.label1 = tk.Label(self.parent, text="Correo", bg="#7EBDC2", fg="#fff")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.label2 = tk.Label(self.parent, text="Contraseña", bg="#7EBDC2", fg="#fff")
        self.label2.grid(row=1, column=0, padx=10, pady=10)
          
        self.entry1 = tk.Entry(self.parent)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)

        self.entry2 = tk.Entry(self.parent, show="*")
        self.entry2.grid(row=1, column=1, padx=10, pady=10)

        self.boton1 = tk.Button(self.parent, text="Ingresar", bg="#fff", command=self.ingresar)
        self.boton1.grid(row=3, column=0, columnspan=2, padx=50, pady=50, sticky=tk.W+tk.E)

    def ingresar(self):
        correo = self.entry1.get()
        contraseña = self.entry2.get()
        if correo == 'quevedo' and contraseña == "1210":
            messagebox.showinfo("Login", "Bienvenido, datos correctos")
        else:
            messagebox.showerror("Login", "Usuario o contraseña son incorrectos")

 



            