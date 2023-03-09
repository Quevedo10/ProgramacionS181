from tkinter import Tk, Frame, Button, Entry, Label, messagebox
from login import login

ventana = Tk()
ventana.title("Ingrese a su correo: ")
ventana.geometry("300x400")
ventana.config(bg="white")


label = Label(ventana, text="correo:",fg="white")
label.pack()

ventana = Tk()
ventana.title("Ingrese a su correo:")
ventana.geometry("800x500")
ventana.config(bg="orange")

label = Label(ventana, text="Correo:",fg="red")
label.pack()
texto_email = Entry(ventana)
texto_email.pack()

label = Label(ventana, text="Contraseña:",fg="red")
label.pack()
texto_password = Entry(ventana, show="*")
texto_password.pack()

def boton_login_click():
     from login import login
     resultado, exitoso = login(texto_email.get(), texto_password.get())
     if exitoso:
         messagebox.showinfo("Su contraseña y usuario son correctos, Bienevenido", resultado)
     else:
         messagebox.showerror("Usuario y contraseña invalida, intente nuevamente", resultado)

boton_login = Button(ventana, text="Iniciar sesión", bg="#66ff99", command=boton_login_click)
boton_login.pack()
ventana.mainloop()