import unittest
from random import choice

from Vehiculo import Vehiculo
from Nuevos import Nuevos
from Usados import Usado
from Nodo import Nodo
from zope.interface.verify import verifyObject
from iColeccion import iColeccion
from Lista import Lista


class VehiculoTest(unittest.TestCase):

    def setUp(self):
        self.vehiculo1 = Vehiculo("Palio", 4, "Rojo", 20000)
        self.vehiculo2 = Vehiculo("Focus", 5, "Azul", 25000)
        self.vehiculo3 = Vehiculo("Corsa", 3, "Blanco", 15000)
        self.vehiculo4 = Vehiculo("Civic", 4, "Gris", 35000)

    def testCrearVehiculo(self):
        self.assertEqual(self.vehiculo1.modelo(), "Palio")
        self.assertEqual(self.vehiculo1.numeroPuertas(), 4)
        self.assertEqual(self.vehiculo1.color(), "Rojo")
        self.assertEqual(self.vehiculo1.precio(), 20000)

    def testObtenerAtributos(self):
        self.assertEqual(self.vehiculo2.modelo(), "Focus")
        self.assertEqual(self.vehiculo2.numeroPuertas(), 5)
        self.assertEqual(self.vehiculo2.color(), "Azul")
        self.assertEqual(self.vehiculo2.precio(), 25000)

    def testInstanciasDistintas(self):
        self.assertIsNot(self.vehiculo3, self.vehiculo4)
        self.assertNotEqual(self.vehiculo3, self.vehiculo4)


class TestNuevos(unittest.TestCase):

    def setUp(self):
        Nuevos.fijarMarca("Marca1")
        self.nuevo1 = Nuevos("Palio", 4, "Rojo", 20000, "Base")
        self.nuevo2 = Nuevos("Focus", 5, "Azul", 25000, "Full")
        self.nuevo3 = Nuevos("Corsa", 3, "Blanco", 15000, "Base")
        self.nuevo4 = Nuevos("Civic", 4, "Gris", 35000, "Full")

    def testCrearNuevo(self):
        self.assertEqual(self.nuevo1.modelo(), "Palio")
        self.assertEqual(self.nuevo1.numeroPuertas(), 4)
        self.assertEqual(self.nuevo1.color(), "Rojo")
        self.assertEqual(self.nuevo1.precio(), 20000)
        self.assertEqual(self.nuevo1.version(), "Base")
        self.assertEqual(self.nuevo1.marca(), "Marca1")

    def testObtenerAtributos(self):
        self.assertEqual(self.nuevo2.modelo(), "Focus")
        self.assertEqual(self.nuevo2.numeroPuertas(), 5)
        self.assertEqual(self.nuevo2.color(), "Azul")
        self.assertEqual(self.nuevo2.precio(), 25000)
        self.assertEqual(self.nuevo2.version(), "Full")
        self.assertEqual(self.nuevo2.marca(), "Marca1")

    def testInstanciasDistintas(self):
        self.assertIsNot(self.nuevo3, self.nuevo4)
        self.assertNotEqual(self.nuevo3, self.nuevo4)


class TestUsado(unittest.TestCase):

    def setUp(self):
        self.usado1 = Usado("Golf", 3, "Negro", 15000
                            , "Marca2", "ABC123", 2018, 90000)
        self.usado2 = Usado("Clio", 5, "Gris", 10000
                            , "Marca2", "DEF456", 2015, 120000)
        self.usado3 = Usado("Corsa", 4, "Blanco", 12000
                            , "Marca2", "GHI789", 2017, 80000)
        self.usado4 = Usado("Fiesta", 3, "Azul", 18000, "Marca2"
                            , "JKL012", 2016, 110000)

    def testCrearUsado(self):
        self.assertEqual(self.usado1.modelo(), "Golf")
        self.assertEqual(self.usado1.numeroPuertas(), 3)
        self.assertEqual(self.usado1.color(), "Negro")
        self.assertEqual(self.usado1.precio(), 15000)
        self.assertEqual(self.usado1.marca(), "Marca2")
        self.assertEqual(self.usado1.patente(), "ABC123")
        self.assertEqual(self.usado1.anio(), 2018)
        self.assertEqual(self.usado1.kilometraje(), 90000)
        self.assertEqual(self.usado1.importeVenta(),
                         15000 * (1 - self.usado1._Usado__descuento()))

    def testObtenerAtributos(self):
        self.assertEqual(self.usado2.modelo(), "Clio")
        self.assertEqual(self.usado2.numeroPuertas(), 5)
        self.assertEqual(self.usado2.color(), "Gris")
        self.assertEqual(self.usado2.precio(), 10000)
        self.assertEqual(self.usado2.marca(), "Marca2")
        self.assertEqual(self.usado2.patente(), "DEF456")
        self.assertEqual(self.usado2.anio(), 2015)
        self.assertEqual(self.usado2.kilometraje(), 120000)
        self.assertEqual(self.usado2.importeVenta(),
                         10000 * (1 - self.usado2._Usado__descuento()))


class TestNodo(unittest.TestCase):

    def setUp(self):
        self.vehiculo1 = Vehiculo("Palio", 4, "Rojo", 20000)
        self.vehiculo2 = Vehiculo("Focus", 5, "Azul", 25000)
        self.vehiculo3 = Vehiculo("Corsa", 3, "Blanco", 15000)
        self.nodo1 = Nodo(self.vehiculo1)
        self.nodo2 = Nodo(self.vehiculo2)
        self.nodo3 = Nodo(self.vehiculo3)

    def testCrearNodo(self):
        self.assertEqual(self.nodo1.getDato(), self.vehiculo1)
        self.assertEqual(self.nodo1.getSiguiente(), None)

    def testEnlazarNodos(self):
        self.nodo1.setSiguiente(self.nodo2)
        self.assertEqual(self.nodo1.getSiguiente(), self.nodo2)

        self.nodo2.setSiguiente(self.nodo3)
        self.assertEqual(self.nodo2.getSiguiente(), self.nodo3)

        self.assertEqual(self.nodo1.getSiguiente().getDato(), self.vehiculo2)
        self.assertEqual(self.nodo1.getSiguiente().getSiguiente().getDato(),
                         self.vehiculo3)
        self.assertEqual(self.nodo1.getSiguiente().getSiguiente().getSiguiente(), None)


class ListaTest(unittest.TestCase):

    def setUp(self):
        self.lista = None
        self.list_nodos = []
        self.vehiculos = []

        # Crear 10 vehículos
        for _ in range(10):
            modelo = choice(["Palio", "Focus", "Corsa"])
            puertas = choice([3, 4, 5])
            color = choice(["Rojo", "Azul", "Blanco"])
            precio = choice([15000, 20000, 25000])

            if choice([True, False]):
                version = choice(["Base", "Full"])
                vehiculo = Nuevos(modelo, puertas, color, precio,
                                  version)
            else:
                marca = choice(["Ford", "Chevrolet", "Fiat"])
                patente = "ABC123"
                anio = choice([2018, 2019, 2020])
                kilometraje = choice([80000, 120000, 150000])
                vehiculo = Usado(modelo, puertas, color, precio,
                                 marca, patente, anio, kilometraje)

            self.vehiculos.append(vehiculo)
        self.cue = None
        self.cab = None
        # Crear nodos con los vehículos
        for vehiculo in self.vehiculos:
            nodo = Nodo(vehiculo)
            self.list_nodos.append(nodo)

    def testCrearLista(self):
        self.lista = Lista(self.list_nodos[0])
        self.assertIsNotNone(self.lista)

    def testObtenerElemento(self):
        self.lista = Lista(self.list_nodos[0])
        self.assertIsNotNone(self.lista.obtenerElemento(0))
        self.assertEqual(self.lista.obtenerElemento(0),
                         self.list_nodos[0])

    def testImplementaiColeccion(self):
        self.lista = Lista()
        self.assertTrue(verifyObject(iColeccion, self.lista))

    def testAgregarElemento(self):
        self.lista = Lista()
        self.lista.agregarElemento(self.list_nodos[0])
        self.assertIsNotNone(self.lista.obtenerElemento(0))
        self.assertEqual(self.lista.obtenerElemento(0),
                         self.list_nodos[0])

    def testInsertarElementoListaVacia(self):
        self.lista = Lista()
        self.lista.insertarElemento(self.list_nodos[0], 5)
        self.assertEqual(self.lista.obtenerElemento(0),
                         self.list_nodos[0])

    def testInsertarElemento(self):
        self.lista = Lista()
        # Agregamos elementos
        self.lista.agregarElemento(self.list_nodos[0])
        self.lista.agregarElemento(self.list_nodos[1])
        self.lista.agregarElemento(self.list_nodos[2])
        # Insertamos elementos en diferentes posiciones
        self.lista.insertarElemento(self.list_nodos[3], 0)
        self.lista.insertarElemento(self.list_nodos[4], 1)
        self.lista.insertarElemento(self.list_nodos[5], 5)
        self.assertEqual(self.lista.obtenerElemento(0),
                         self.list_nodos[3])
        self.assertEqual(self.lista.obtenerElemento(1),
                         self.list_nodos[4])
        self.assertEqual(self.lista.obtenerElemento(5),
                         self.list_nodos[5])

    def testIterador(self):
        self.lista = Lista()
        for v in self.vehiculos:
            self.lista.agregarVehiculo(v)

        iterador = iter(self.lista)

        for vehiculo in self.vehiculos:
            iv = next(iterador)
            self.assertEqual(iv, vehiculo)

        with self.assertRaises(StopIteration):
            next(iterador)

    def testAgregarVehiculo(self):
        self.lista = Lista()
        for vehiculo in self.vehiculos:
            self.lista.agregarVehiculo(vehiculo)

        self.assertEqual(self.lista.obtenerElemento(0).getDato(),
                         self.vehiculos[0])
        self.assertEqual(self.lista.obtenerElemento(len(self.vehiculos)-1).getDato(),
                         self.vehiculos[-1])



if __name__ == '__main__':
    unittest.main()
