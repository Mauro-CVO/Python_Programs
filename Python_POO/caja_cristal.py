import unittest

def mayor_de_edad(edad):
    if edad >= 18:
        return False
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_si_mayor(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)
    
    def test_menor(self):
        edad = 10

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)





if __name__ == "__main__":
    unittest.main()