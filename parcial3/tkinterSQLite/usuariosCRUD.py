from logging import root
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import controladorBD

# Creamos un objeto de la clase controladorBD
controlador = controladorBD()

# Función para disparar el botón
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(),varCor.get(),varCon.get())

# Función para disparar el boton de busqueda
def ejecutaSelectU():
   usuario = controlador.consultarUsuario(varBus.get())
   for usu in usuario:
    
    cadena = str(usu[0])+ " " + usu[1]+ " " + usu[2]+ " " + str(usu[3])

   if(usuario):
       textEnc.insert("0.0",cadena)
   else:
       messagebox.showinfo("Usuario no encontrado","Seguramente no exita en la base de datos")

def ejecutarConsulta():
   usuarios = controlador.impUsuario()
   treeview.delete(*treeview.get_children())
   if usuarios:
      for usuario in usuarios:
         treeview.insert("","end", values = (usuario[0], usuario[1], usuario[2], usuario[3]))
   else:
      messagebox.showinfo("No existe usuarios","No encontramos usuarios en la base de datos")


def ejecutaUpdate():
    idUsuario = varIdUp.get()
    nombreUsuario = varNomUp.get()
    correoUsuario = varCorUp.get()
    contrasenaUsuario = varConUp.get()
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro que deseas actualizar los datos del usuario?")
    if confirmacion:
        controlador.actualizarUsuario(idUsuario, nombreUsuario, correoUsuario, contrasenaUsuario)
        messagebox.showinfo("Actualización exitosa", "Los datos del usuario han sido actualizados en la base de datos.")
    else:
        messagebox.showinfo("Actualización cancelada", "Los datos del usuario no han sido actualizados en la base de datos.")

def ejecutaDelete():
    idUsuario = varIdDel.get()
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro que deseas eliminar al usuario seleccionado?")
    if confirmacion:
        controlador.elimUsuario(idUsuario)
        messagebox.showinfo("Eliminación exitosa", "El usuario ha sido eliminado de la base de datos.")
    else:
        messagebox.showinfo("Eliminación cancelada", "El usuario no ha sido eliminado de la base de datos.")

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestaña1 = ttk.Frame(panel)
pestaña2 = ttk.Frame(panel)
pestaña3 = ttk.Frame(panel)
pestaña4 = ttk.Frame(panel)
pestaña5 = ttk.Frame(panel)

# Pestaña1: Formulario de usuarios

Label(pestaña1, text='Registro de usuarios', fg='blue', font=('Modern', 18)).pack()

varNom = StringVar()
Label(pestaña1, text="Nombre: ").pack()
Entry(pestaña1, textvariable=varNom).pack()

varCor = StringVar()
Label(pestaña1, text="Correo: ").pack()
Entry(pestaña1, textvariable=varCor).pack()

varCon = StringVar()
Label(pestaña1, text="Contraseña: ").pack()
Entry(pestaña1, textvariable=varCon, show="*").pack()

btnGuardar = Button(pestaña1, text="Guardar Usuario", command=ejecutaInsert)
btnGuardar.pack()

#Pestaña 2: Buscar Usuarios

titulo2 = Label(pestaña2,text="Buscar Usuario", fg='green', font=("Modern",18)).pack()

varBus = tk.StringVar()
lblid = Label(pestaña2,text= "Identificador de usuarios: ").pack()
txtid = Entry(pestaña2,textvariable=varBus).pack()
btnBus = Button(pestaña2, text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestaña2,text="Encontrado: ", fg='blue', font=("Modern",15)).pack()
textEnc = tk.Text(pestaña2,height=5,width=52)
textEnc.pack()

#Pestaña 3: Consultar usuarios

titulo3 = Label(pestaña3,text="Consultar Usuarios", fg='green', font=("Modern",18)).pack()

varCons = tk.StringVar()
botonCons = Button(pestaña3, text = "Buscar", command=ejecutarConsulta).pack()

treeview = ttk.Treeview(pestaña3, columns=(1,2,3,4), show = "headings", height="5")
treeview.heading(1, text="id")
treeview.column(1, width=10)
treeview.heading(2, text="Nombre_Usuario")
treeview.column(2, width=60)
treeview.heading(3, text="Correo_Usuario")
treeview.column(3, width=50)
treeview.heading(4, text="Contraseña_Uusario")
treeview.column(4, width=30)

subCons = Label(pestaña3, text="Usuarios que se encontraron: ", fg="black",font=("Modern",18)).pack()
treeview.pack()

#Pestaña 4: Actualizar Usuario

titulo4 = Label(pestaña4,text="Actualizar y Eliminar", fg='blue', font=("Modern",18)).pack()

varIdUp = StringVar()
Label(pestaña4, text="ID de Usuario a Actualizar: ").pack()
Entry(pestaña4, textvariable=varIdUp).pack()

varNomUp = StringVar()
Label(pestaña4, text="Nombre de Usuario Nuevo: ").pack()
Entry(pestaña4, textvariable=varNomUp).pack()

varCorUp = StringVar()
Label(pestaña4, text="Correo de Usuario Nuevo: ").pack()
Entry(pestaña4, textvariable=varCorUp).pack()

varConUp = StringVar()
Label(pestaña4, text="Contraseña de Usuario Nueva: ").pack()
Entry(pestaña4, textvariable=varConUp, show="*").pack()

btnActualizar = Button(pestaña4, text="Actualizar", command=ejecutaUpdate)
btnActualizar.pack()

#Pestaña 5: Eliminar Usuario

titulo5 = Label(pestaña5,text="Eliminar Usuario", fg='blue', font=("Modern",18)).pack()

varIdDel = StringVar()
Label(pestaña5, text="ID de Usuario a Eliminar: ").pack()
Entry(pestaña5, textvariable=varIdDel).pack()

btnEliminar = Button(pestaña5, text="Eliminar Usuario", command=ejecutaDelete)
btnEliminar.pack()

panel.add(pestaña1, text='Formulario de usuarios')
panel.add(pestaña2, text='Buscar usuario')
panel.add(pestaña3, text='Consultar usuarios')
panel.add(pestaña4, text='Actualizar usuario')
panel.add(pestaña5, text='Eliminar usuario')

ventana.mainloop()