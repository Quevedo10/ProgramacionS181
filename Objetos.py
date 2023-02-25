
#1. Importar la clase
from Personaje import *

#2. Solicitar atributos para el objeto
print("")
print("### Solicitud de datos del Héroe ###")
espH = input ("Escrible la especie del Héroe: ")
nomH = input ("Escrible el nombre del Héroe: ")
altH = float (input ("Escrible la altura del Héroe: "))
cargaH = int (input ("Cuantas balas se le recargarán al Héroe: "))

print("")
print("### Solicitud de datos del Villano ###")
espV = input ("Escrible la especie del Villano: ")
nomV = input ("Escrible el nombre del Villano: ")
altV = float (input ("Escrible la altura del Villano: "))
cargaV = int (input ("Cuantas balas se le recargarán al Villano: "))

#3. Creamos 2 objetos

Heroe = Personaje(espH, nomH, altH)
Villano = Personaje(espV, nomV, altV)

#Ejemplo del uso del set
Heroe.setNombre("Quevedo")

#4. Acceder a atributos y métodos de cada OBJETO

print("")
print("### Atributos y Metodos del Héroe ###")
print("El personaje pertenece a la raza: "+ Heroe.getEspecie())
print("El personaje se llama: "+ Heroe.getNombre())
print("El personaje mide: "+ str(Heroe.getAltura()) +" metros")

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(cargaH)
#Heroe.__pensar()

print("")
print("### Atributos y Metodos del Villano ###")
print("El personaje pertenece a la raza: "+ Villano.getEspecie())
print("El personaje se llama: "+ Villano.getNombre())
print("El personaje mide: "+ str(Villano.getAltura()) +" metros")

Villano.correr(True)
Villano.lanzarGranada()
Villano.recargarArma(cargaV)
