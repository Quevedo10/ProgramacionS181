
class Personaje:

    #atributos del personaje
    
    especie = "Humano"
    nombre = "Dom"
    altura = 1.85

    #Metodos del personaje

    def correr(self, status):
        if(status):
            print("El personaje "+ self.nombre + "ésta corriendo.")
        else:
            print("El personaje "+ self.nombre + "se detuvo.")
    
    def lanzarGranada(self):
        print("Se lanzó granada ")

    def recargarArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene ahora "+ cargador + "balas")
