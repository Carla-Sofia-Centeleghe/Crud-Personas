# Parte del codigo que manipula los objetos
# Carla S. Centeleghe

from persona import Persona
import re


class PersonaService:
    def __init__(self):
        self.persona = {}

    # Crea un archivo
    def createFile(self):
        create = input('Nombre archivo: ')
        archivo = f'{create}.txt'
        archivo = open(archivo, 'w')
        archivo.close()
        return archivo

    # Escribe/Rellena el archivo con los datos de la persona
    def writeFile(self, persona):
        archivo = input(
            'Vamos a escribir un archivo para una persona, eleja una nombre para el archivo: ')
        persona.documento = int(input('Documento: '))
        persona.apellido = input('Apellido: ')
        persona.nombre = input('Nombre: ')
        with open(archivo, 'a') as archivo:
            archivo.write(
                f'\nDocumento: {persona.documento}, Apellido: {persona.apellido}, Nombre: {persona.nombre}')

    # Agrega una persona / solo impreme lo ingresado por terminal
    def add(self, persona):
        print('Agregemos una persona\n')
        # persona.documento = int(input('Documento: '))
        # persona.apellido = input('Apellido: ')
        # persona.nombre = input('Nombre: ')
        # print(persona.documento, persona.apellido, persona.nombre)
        self.persona.append(persona)

    # Elimina
    def delete(self, persona):
        # documento = int(input('Docuemnto de la persona a eliminar: '))
        self.persona.remove(persona)

    #Busca por documento
    def findByDocumento(self, documento: int):
        try:
            return self.persona[documento]
        except KeyError:
            print('Documento no valido')
            return None

    # Devuelbe persona
    def findAll(self):
        return self.persona


