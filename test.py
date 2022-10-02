# Test personas
# Carla S. Centeleghe

import unittest
from persona import Persona

class TestPersona(unittest.TestCase):
    def testPersona_1(self):
        persona = Persona(42318947, 'Centeleghe', 'Carla')
        self.assertEqual(persona.__dict__, {
                         'documento': 42318947, 'apellido': 'Centeleghe', 'nombre': 'Carla'})

    def testPersona_2(self):
        persona = Persona(1, 'Hongito', 'Pepe')
        self.assertEqual(persona.__dict__,
                         {'documento': 1, 'apellido': 'Hongito', 'nombre': 'Pepe'})

if __name__ == '__main__':
    unittest.main()
