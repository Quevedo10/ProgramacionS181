class logica:

    numero_romano = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        11: "XI",
        12: "XII",
        13: "XIII",
        14: "XIV",
        15: "XV",
        16: "XVI",
        17: "XVII",
        18: "XVIII",
        19: "XIX",
        20: "XX",
        21: "XXI",
        22: "XXII",
        23: "XXIII",
        24: "XXIV",
        25: "XXV",
        26: "XXVI",
        27: "XXVII",
        28: "XXVIII",
        29: "XXIX",
        30: "XXX",
        31: "XXXI",
        32: "XXXII",
        33: "XXXIII",
        34: "XXXIV",
        35: "XXXV",
        36: "XXXVI",
        37: "XXXVII",
        38: "XXXVIII",
        39: "XXXIX",
        40: "XL",
        41: "XLI",
        42: "XLII",
        43: "XLIII",
        44: "XLIV",
        45: "XLV",
        46: "XLVI",
        47: "XLVII",
        48: "XLVIII",
        49: "XLIX",
        50: "L"
    }

    numero_arabico = {
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 4,
        "V": 5,
        "VI": 6,
        "VII": 7,
        "VIII": 8,
        "IX": 9,
        "X": 10,
        "XI": 11,
        "XII": 12,
        "XIII": 13,
        "XIV": 14,
        "XV": 15,
        "XVI": 16,
        "XVII": 17,
        "XVIII": 18,
        "XIX": 19,
        "XX": 20,
        "XXI": 21,
        "XXII": 22,
        "XXIII": 23,
        "XXIV": 24,
        "XXV": 25,
        "XXVI": 26,
        "XXVII": 27,
        "XXVIII": 28,
        "XXIX": 29,
        "XXX": 30,
        "XXXI": 31,
        "XXXII": 32,
        "XXXIII": 33,
        "XXXIV": 34,
        "XXXV": 35,
        "XXXVI": 36,
        "XXXVII": 37,
        "XXXVIII": 38,
        "XXXIX": 39,
        "XL": 40,
        "XLI": 41,
        "XLII": 42,
        "XLIII": 43,
        "XLIV": 44,
        "XLV": 45,
        "XLVI": 46,
        "XLVII": 47,
        "XLVIII": 48,
        "XLIX": 49,
        "L": 50
    }

    def convert(self, ingresar_value):
        if ingresar_value.isdigit():
            numArabigo = int(ingresar_value)
            if numArabigo < 1 or numArabigo > 50:
                raise ValueError("Número que agregaste es mayor del 1 al 50.")
            return self.arabigoAromano(numArabigo)
        else:
            numero_romano = ingresar_value.upper()
            if numero_romano not in self.numero_arabico:
                raise ValueError("Ingresa números válidos")
            return self.numero_arabico[numero_romano]

    def arabigoAromano(self, numArabigo):
        if numArabigo in self.numero_romano:
            return self.numero_romano[numArabigo]
        else:
            numero_romano = ""
            for validar_arabigo, validar_romano in reversed(list(self.numero_romano.items())):
                while numArabigo >= validar_arabigo:
                    numero_romano += validar_romano
                    numArabigo -= validar_arabigo
            return numero_romano

