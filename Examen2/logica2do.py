import random
from tkinter import tk

class logica2do:

    def generar_matricula():
        
        nombre = nombre.entry.get()
        apellidoPa = apellidoPa.entry.get()
        apellidoMa = apellidoMa.entry.get()
        año_nacimiento = año_nacimiento.entry.get()
        carrera = carrera.entry.get()

        letra_nombre = nombre[0]
        letra_apellidoPa = apellidoPa[2]
        letra_apellidoMa = apellidoMa[2]
        año_nacimiento = año_nacimiento[2]
        letra_carrera = carrera[3]
        aleat = str(random.randint(0, 99))[2]
        matricula = letra_nombre + letra_apellidoPa + letra_apellidoMa + año_nacimiento + letra_carrera + aleat
        
        matricula.config(text="Matrícula generada: " + matricula)
