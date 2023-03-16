class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad

    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            self.saldo -= cantidad

    def depositar_otra_cuenta(self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            print("No tienes suficiente saldo para realizar esa transferencia.")
        else:
            self.saldo -= cantidad
            otra_cuenta.ingresar_efectivo(cantidad)