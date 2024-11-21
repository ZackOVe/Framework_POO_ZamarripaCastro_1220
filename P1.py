print ("")
print ("Zamarripa Castro Erick Fabian 3W 1220")
print ("")

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"
    print ("")
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso
if __name__ == "__main__":
    persona1 = Persona("Juan", 20, "5674563456")
    print(persona1.mostrar())
    print("Es mayor de edad:", persona1.es_mayor_de_edad())

    persona2 = Persona("Ana", 17, "TR4534532334")
    print(persona2.mostrar())
    print("Es mayor de edad:", persona2.es_mayor_de_edad())
print ("")