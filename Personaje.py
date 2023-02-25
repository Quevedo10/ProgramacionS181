
class Personaje:
    
    def __init__(self, esp, nom, alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt

    #Metodos del personaje

    def correr(self, status):
        if(status):
            print("El personaje "+ self.__nombre + " ésta corriendo.")
        else:
            print("El personaje "+ self.__nombre + " se detuvo.")
    
    def lanzarGranada(self):
        print("Se lanzó granada ")

    def recargarArma(self, municiones):
        cargador = 5
        cargador = cargador + municiones
        print("El arma tiene ahora "+ str(cargador) + " balas")

    #Ejemplo de metodo privado
    #def __pensar(self):
    #   print("Estoy pensando...")

    #Declaramos los getters and setters de los atributos privados

    def getEspecie(self):
        return self.__especie

    def setEspecie(self,esp):
        self.__especie = esp

    def getNombre(self):
        return self.__nombre

    def setNombre(self,nom):
        self.__nombre = nom

    def getAltura(self):
        return self.__altura

    def setAltura(self,alt):
        self.__altura = alt

         