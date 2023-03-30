from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:

    def __init__(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):

        try:
            conexion = sqlite3.connect("C:/Users/migue/OneDrive/Documentos/GitHubPOO/ProgramacionS181/parcial3/tkinterSQLite/DBUsuarios.db")
            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")

    #Metodo para guardar usuarios
    def guardarUsuario(self,nom,cor,con):

        # paso 1: usamos una conexion
        conx = self.conexionBD()

        # paso 2: validar parametros que esten vacios
        if(nom=="" or cor=="" or con ==""):
            messagebox.showwarning("Formulario Incompleto")
        else:
        # paso 3: preparamos el cursor, datos y QuerySQL
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom,cor,conH)
            qrInsert = "insert into TBRegistrados(nombre,correo,contraseña) values(?,?,?)"

        # paso 4: ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")

    def encriptarCon(self,con):
        conPlana = con
        conPlana = conPlana.encode() #convertimos con a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(conPlana,sal)
        print(conHa)

        #enviamos la contraseña encryptada
        return conHa

     # Metodo para buscar un usuario
    def consultarUsuario(self,id):
        #1. Preparar una conexion
        cons = self.conexionBD()

        #2. Verifiacar si ID contiene algo
        if(id == ""):
            messagebox.showwarning("Cuidado","ID vacío")
            cons.close()
        else:
            try:
                #3. Preparar cursor y querry
                cursor = cons.cursor()
                selecQuery = "select * from TBRegistrados where id="+id

                #4. Ejecutar y guardar la consulta
                cursor.execute(selecQuery)
                rsUsuario = cursor.fetchall()
                cons.close()

                return rsUsuario

            except sqlite3.OperationalError:
                print("Error consulta")