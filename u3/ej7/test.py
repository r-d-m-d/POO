import unittest

from Personal import Personal
from PersonalDeApoyo import PersonalDeApoyo
from Docente import Docente
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador

CATEGORIA_1_10 = 5
CATEGORIA_11_20 = 15
CATEGORIA_21 = 22


class PersonalDeApoyoTests(unittest.TestCase):
    def setUp(self):
        self.personal1 = PersonalDeApoyo(
            cuil='123456789',
            apellido='Pérez',
            nombre='Juan',
            sueldo_basico=50000,
            antiguedad=5,
            categoria=CATEGORIA_1_10
        )

        self.personal2 = PersonalDeApoyo(
            cuil='987654321',
            apellido='Gómez',
            nombre='María',
            sueldo_basico=60000,
            antiguedad=3,
            categoria=CATEGORIA_11_20
        )

        self.personal3 = PersonalDeApoyo(
            cuil='456789123',
            apellido='López',
            nombre='Carlos',
            sueldo_basico=55000,
            antiguedad=8,
            categoria=CATEGORIA_21
        )

    def test_cuil(self):
        self.assertEqual(self.personal1.cuil(), '123456789')
        self.assertEqual(self.personal2.cuil(), '987654321')
        self.assertEqual(self.personal3.cuil(), '456789123')

    def test_apellido(self):
        self.assertEqual(self.personal1.apellido(), 'Pérez')
        self.assertEqual(self.personal2.apellido(), 'Gómez')
        self.assertEqual(self.personal3.apellido(), 'López')

    def test_nombre(self):
        self.assertEqual(self.personal1.nombre(), 'Juan')
        self.assertEqual(self.personal2.nombre(), 'María')
        self.assertEqual(self.personal3.nombre(), 'Carlos')

    def test_sueldo_basico(self):
        self.assertEqual(self.personal1.sueldo_basico(), 50000)
        self.assertEqual(self.personal2.sueldo_basico(), 60000)
        self.assertEqual(self.personal3.sueldo_basico(), 55000)

    def test_antiguedad(self):
        self.assertEqual(self.personal1.antiguedad(), 5)
        self.assertEqual(self.personal2.antiguedad(), 3)
        self.assertEqual(self.personal3.antiguedad(), 8)

    def test_categoria(self):
        self.assertEqual(self.personal1.categoria(), CATEGORIA_1_10)
        self.assertEqual(self.personal2.categoria(), CATEGORIA_11_20)
        self.assertEqual(self.personal3.categoria(), CATEGORIA_21)

    def test_bono_por_antiguedad(self):
        self.assertEqual(self.personal1.bono_por_antiguedad(), 2500)
        self.assertEqual(self.personal2.bono_por_antiguedad(), 1800)
        self.assertEqual(self.personal3.bono_por_antiguedad(), 4400)

    def test_bono_por_categoria(self):
        self.assertEqual(self.personal1.bono_por_categoria(), 5000)
        self.assertEqual(self.personal2.bono_por_categoria(), 12000)
        self.assertEqual(self.personal3.bono_por_categoria(), 16500)

    def test_sueldo(self):
        self.assertEqual(self.personal1.sueldo(), 57500)
        self.assertEqual(self.personal2.sueldo(), 73800)
        self.assertEqual(self.personal3.sueldo(), 75900)


class DocenteTests(unittest.TestCase):
    def setUp(self):
        self.docente1 = Docente(
            cuil='123456789',
            apellido='Pérez',
            nombre='Juan',
            sueldo_basico=50000,
            antiguedad=5,
            carrera='Informática',
            cargo='simple',
            catedra='Programación'
        )

        self.docente2 = Docente(
            cuil='987654321',
            apellido='Gómez',
            nombre='María',
            sueldo_basico=60000,
            antiguedad=3,
            carrera='Matemáticas',
            cargo='semiexclusivo',
            catedra='Álgebra'
        )

        self.docente3 = Docente(
            cuil='456789123',
            apellido='López',
            nombre='Carlos',
            sueldo_basico=55000,
            antiguedad=8,
            carrera='Física',
            cargo='exclusivo',
            catedra='Mecánica Cuántica'
        )

    def test_carrera(self):
        self.assertEqual(self.docente1.carrera(), 'Informática')
        self.assertEqual(self.docente2.carrera(), 'Matemáticas')
        self.assertEqual(self.docente3.carrera(), 'Física')

    def test_cargo(self):
        self.assertEqual(self.docente1.cargo(), 'simple')
        self.assertEqual(self.docente2.cargo(), 'semiexclusivo')
        self.assertEqual(self.docente3.cargo(), 'exclusivo')

    def test_catedra(self):
        self.assertEqual(self.docente1.catedra(), 'Programación')
        self.assertEqual(self.docente2.catedra(), 'Álgebra')
        self.assertEqual(self.docente3.catedra(), 'Mecánica Cuántica')

    def test_bono_por_cargo(self):
        self.assertEqual(self.docente1.bono_por_cargo(), 5000)
        self.assertEqual(self.docente2.bono_por_cargo(), 12000)
        self.assertEqual(self.docente3.bono_por_cargo(), 27500)

    def test_sueldo(self):
        self.assertEqual(self.docente1.sueldo(), 57500)
        self.assertEqual(self.docente2.sueldo(), 73800)
        self.assertEqual(self.docente3.sueldo(), 86900)


class InvestigadorTests(unittest.TestCase):
    def setUp(self):
        self.investigador1 = Investigador(
            cuil='123456789',
            apellido='Pérez',
            nombre='Juan',
            sueldo_basico=50000,
            antiguedad=5,
            area='Ciencias Naturales',
            tipo='Experimental'
        )

    def test_area(self):
        self.assertEqual(self.investigador1.area(), 'Ciencias Naturales')

    def test_tipo(self):
        self.assertEqual(self.investigador1.tipo(), 'Experimental')

    def test_sueldo(self):
        self.assertEqual(self.investigador1.sueldo(), 52500)



class DocenteInvestigadorTests(unittest.TestCase):
    def setUp(self):
        self.docente_investigador1 = DocenteInvestigador(
            cuil='123456789',
            apellido='Pérez',
            nombre='Juan',
            sueldo_basico=50000,
            antiguedad=5,
            carrera='Informática',
            cargo='simple',
            catedra='Programación',
            categoria_investigacion='Categoría 1',
            importe_extra=10000,
            area='Ciencias Naturales',
            tipo='Experimental'
        )

    def test_categoria_investigacion(self):
        self.assertEqual(self.docente_investigador1.categoria_investigacion(), 'Categoría 1')

    def test_importe_extra(self):
        self.assertEqual(self.docente_investigador1.importe_extra(), 10000)

    def test_sueldo(self):
        self.assertEqual(self.docente_investigador1.sueldo(), 67500)


if __name__ == '__main__':
    unittest.main()
