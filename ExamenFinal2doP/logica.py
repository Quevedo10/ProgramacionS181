class numRomano:
    def __init__(self):
        self.numeroRomano = (('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))

    def romanoConvertido(self, numero):
        if not 0 < numero < 51:
            raise ValueError("Número no válido en el rango permitido")

        result = '' 
        for romano, arabigo in self.numeroRomano:
            while numero >= arabigo:
                result += romano
                numero -= arabigo

        if numero != 0:
            result = None

        return result
    def arabigo(self, romanoNumero):
        if not isinstance(romanoNumero, str):
            raise TypeError("El número romano debe ser una cadena de texto")
        romanoNumero = romanoNumero.upper()
        result = 0
        ingres = 0
        for romano, arabigoo in self.numeroRomano:
            while romanoNumero[ingres:ingres + len(romano)] == romano:
                result += arabigoo
                ingres += len(romano)
        if result is None:
            raise ValueError(f"El número romano '{romanoNumero}' no es válido")
        elif result > 50:
            raise ValueError("El número arábigo es mayor que 50")
        return result

