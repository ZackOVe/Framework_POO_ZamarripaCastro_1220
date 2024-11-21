print ("")
print ("Zamarripa Castro Erick Fabian 3W 1220")
print ("")

#Clase de cuenta, se definen las cantidades o titular
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def retirar(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
            print(f"Se ha retirado {cantidad} de la cuenta YEIII.")
        else:
            print("No hay suficiente para realizar la retirada (POBRE).")
    print ("")
    def mostrar(self):
        return f"Titular: {self.titular}, Saldo: {self.cantidad}"

#Clase de CuentaJoven, se define cantidad, titular y bonificacion
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    
    def esTitularValido(self):
        if 18 <= self.titular['edad'] < 25:
            return True
        return False


    def retirar(self, cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print("No puedes retirar dinero porque no eres invalido (down).")
    print ("")
    
    def mostrar(self):
        return f"Cuenta Joven con bonificación del {self.bonificacion}%. Titular: {self.titular['nombre']}, Saldo: {self.cantidad}"

#Uso correcto
titular1 = {'nombre': 'Dylan El Papá', 'edad': 100}
print ("")
cuenta1 = CuentaJoven(titular1, 1000, 5) 

print(cuenta1.mostrar())  
cuenta1.retirar(200) 
cuenta1.retirar(1000)  

titular2 = {'nombre': 'Jared Fandelos Femboy', 'edad': 7}
print ("")
cuenta2 = CuentaJoven(titular2, 1500, 7) 

print(cuenta2.mostrar()) 
cuenta2.retirar(100)  
print ("")