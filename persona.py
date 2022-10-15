# Parte del codigo dedicada a la persona
# Carla S. Centeleghe

class Persona:
    def __init__(self, documento=int, apellido=str, nombre=str):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __repr__(self):
        return f'Persona: {self.documento} - {self.apellido} - {self.nombre}'

    def input(self):
       self.documento = int(input('Ingrese documento: '))
       self.apellido = input('Ingrese apellido: ')
       self.nombre = input('Ingrese nombre: ')


if __name__ == "__main__":
    documento = int(input("Ingrese documento: "))
    apellido = str(input("Ingrese apellido: "))
    nombre = str(input("Ingrese nombre: "))
    print(Persona(documento, apellido, nombre))
