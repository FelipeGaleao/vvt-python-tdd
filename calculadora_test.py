from calculadora import Calculadora
import unittest

class TestCalculadora(unittest.TestCase):
    ## Usamos a função setUp para criar uma instância da classe Calculadora que será usada em todos os todos
    ## os casos de teste a seguir

    def setUp(self):
        self.calc = Calculadora()

    def test_soma(self):
        self.assertEqual(self.calc.soma(2, 4), 6)

    def test_subtracao(self):
        self.assertEqual(self.calc.subtracao(4, 2), 2)

    def test_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(2, 5), 10)

    def test_divisao(self):
        self.assertEqual(self.calc.divisao(10, 2), 5)

    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divisao, 10, 0)
