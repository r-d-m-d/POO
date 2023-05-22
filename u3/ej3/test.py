import unittest

import Persona
import Taller

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.p = Persona.Persona("Juan","Perez","41234567")

    def testCreacion(self):
        self.assertTrue(False)


class TestTaller(unittest.TestCase):

    def setUp(self):
        self.t = Taller.Taller(1,"Herreria", 5, 2500)

    def testCreacion(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
