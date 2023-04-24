import random
import string


class generadorContra:
    def __init__(self, longitud=8, mayusculas=True, caracteres=True):
        self._longitud = longitud
        self._mayusculas = mayusculas
        self._caracteres = caracteres

    def set_longitud(self, longitud):
        self._longitud = longitud

    def mayusculas(self, mayusculas):
        self._mayusculas = mayusculas

    def caracteres(self, caracteres):
        self._caracteres = caracteres

    def contrasenaGenerada(self):
        caract = string.ascii_lowercase
        if self._mayusculas:
            caract += string.ascii_uppercase
        if self._caracteres:
            caract += string.punctuation

        cont = "".join(random.choice(caract) for _ in range(self._longitud))
        return cont
    



     








    

