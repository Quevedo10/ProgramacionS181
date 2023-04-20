
import sqlite3
import tkinter
import tkinter as tk
from tkinter import messagebox

class controlador:

    def __init__(self):
        pass

    # Metodo para crear conexiones
    def conexionBD(self):


        try:
            conexion = sqlite3.connect("Ferreteria.db")

            print("Conectado a la Base de Datos")
            return conexion
        except sqlite3.OperationalError:
            print("No se puede conectar")
            from tkinter import messagebox

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
            qrInsert = "insert into MatConstruccion(IDMat, Material, Cantidad) values(?,?,?)"


        # paso 4: ejecutar Insert y cerramos conexion
            cursor.execute(qrInsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado")


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
                selecQuery = "select * from MatConstruccion where IDMat="+id


                #4. Ejecutar y guardar la consulta
                cursor.execute(selecQuery)
                rsUsuario = cursor.fetchall()
                cons.close()

                return rsUsuario

            except sqlite3.OperationalError:
                print("Error consulta")

    def impUsuario(self):
        cons = self.conexionBD()

        try:
            cursor = cons.cursor()
            selectQuery = "select * from MatConstruccion"


            cursor.execute(selectQuery)
            rsUsuarios = cursor.fetchall()
            cons.close()

            return rsUsuarios
        
        except sqlite3.OperationalError:
            print("Error de Consulta")

        # Método para actualizar un usuario
    def actualizarUsuario(self, id, nom, cor, con):
        # 1. Preparar una conexión
        cons = self.conexionBD()

        # 2. Verificar si el ID está vacío
        if(id == ""):
            messagebox.showwarning("Cuidado","ID vacío")
            cons.close()
        else:
            try:
                # 3. Preparar cursor y query
                cursor = cons.cursor()

                # 4. Encriptar la contraseña si es necesario
                if con != "":
                    con = self.encriptarCon(con)

                # 5. Actualizar los datos del usuario
                updQuery = f"UPDATE MatConstruccion SET Material=?, Cantidad=? WHERE IDMat={id}"
                datos = (nom, con)
                cursor.execute(updQuery, datos)


                # 6. Guardar los cambios y cerrar la conexión
                cons.commit()
                cons.close()

                messagebox.showinfo("Exito", "Usuario actualizado")
            except sqlite3.OperationalError:
                print("Error actualizando usuario")