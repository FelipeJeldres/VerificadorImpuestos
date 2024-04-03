class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

class Ciudadano(Persona):
    def __init__(self, nombre, edad, deposito):
        super().__init__(nombre, edad)
        self.deposito = deposito

    def imprimir(self):
        super().imprimir()
        print(f"Depósito: ${self.deposito}")

    def impuestos(self):
        if self.deposito > 4000:
            print("Sí debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")

# Datos para el ejercicio
datos_ciudadanos = [
    ("Manuel Chima", 25, 6700),
    ("Fayle García", 56, 3500),
    ("Lesly Rodríguez", 34, 9000),
    ("Mario Herrera", 45, 2500)
]

# Crear objetos Ciudadano y llamar al método impuestos
for nombre, edad, deposito in datos_ciudadanos:
    ciudadano = Ciudadano(nombre, edad, deposito)
    ciudadano.imprimir()
    ciudadano.impuestos()
    print()
    
