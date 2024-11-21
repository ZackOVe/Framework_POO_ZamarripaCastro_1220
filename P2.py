print ("")
print ("Zamarripa Castro Erick Fabian 3W 1220")
print ("")
# Ejercicio 2: Clase Cuenta
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        if not isinstance(value, str) or len(value) != 9:
            raise ValueError("El DNI debe ser una cadena de 9 caracteres.")
        self._dni = value

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        #Valida el titular 
        if not isinstance(titular, Persona):
            raise ValueError("El titular debe ser una instancia de la clase Persona.")
        self.titular = titular
        self._cantidad = float(cantidad)

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        #Permite ingresar positivas
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        #Permite retirar cualquier cantidad, incluso dejando saldo negativo
        self._cantidad -= cantidad

    def mostrar(self):
        #Devuelve un mensaje de datos
        return f"Titular: {self.titular.mostrar()}, Cantidad: {self.cantidad:.2f}"

#Permite retirar una cantidad deseada
try:
    persona1 = Persona("Dylan gay salchicha", 30, "666777888")
    cuenta = Cuenta(persona1, 500.0)

    print(cuenta.mostrar())  
    cuenta.ingresar(200)     
    cuenta.retirar(100)      
    print(cuenta.mostrar())  
except Exception as e:
    print(f"Error: {e}")
    print("")