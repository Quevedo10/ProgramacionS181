import tkinter as tk

# Definir la función para generar la matrícula
def generar_matricula():
    #Obtener los valores ingresados por el usuario
    Edificio =  edificio_entry.get()
    nombre = nombre_entry.get()
    apellidos = apellidos_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    carrera = carrera_entry.get()
    
    # Generar la matrícula
    letra_Edificio = Edificio[0]
    letra_nombre = nombre[0]
    letra_apellido = apellidos[0]
    año_nacimiento = fecha_nacimiento[-4:]
    digitos_nacimiento = año_nacimiento[2:]
    letra_carrera = carrera[0]
    aleat = str(random.randint(0, 99))[2]
    matricula = letra_Edificio + letra_nombre + letra_apellido + digitos_nacimiento + letra_carrera + aleat
    
    # Actualizar la etiqueta de la matrícula
    matricula_label.config(text="Matrícula generada: " + matricula)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Matrículas UPQ")
ventana.geometry("600x400")

# crear etiqueta en qué municipio vive el alumno
edificio_label = tk.Label(ventana, text="Edificio: ")
edificio_label.pack()
edificio_entry = tk.Entry(ventana)
edificio_entry.pack()

# Crear etiquetas y campos de entrada
nombre_label = tk.Label(ventana, text="Nombre: ")
nombre_label.pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack()

apellidos_label = tk.Label(ventana, text="Apellidos: ")
apellidos_label.pack()
apellidos_entry = tk.Entry(ventana)
apellidos_entry.pack()

fecha_nacimiento_label = tk.Label(ventana, text="Fecha de Nacimiento: ")
fecha_nacimiento_label.pack()
fecha_nacimiento_entry = tk.Entry(ventana)
fecha_nacimiento_entry.pack()

carrera_label = tk.Label(ventana, text="Carrera: ")
carrera_label.pack()
carrera_entry = tk.Entry(ventana)
carrera_entry.pack()

# Crear el botón para generar la matrícula
generar_matricula_button = tk.Button(ventana, text="Aceptar", command=generar_matricula)
generar_matricula_button.pack()

# Crear la etiqueta para mostrar la matrícula
matricula_label = tk.Label(ventana, text="")
matricula_label.pack()

# Ejecutar la ventana principal
ventana.mainloop()
