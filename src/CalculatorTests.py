import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

        def test_results_property_calculator(self):
            calculator = Calculator()
            self.assertEqual(calculator.result, 6)

        def test_add_method_calculator(self):
            calculator = Calculator()
            self.assertEqual(calculator.add(3, 3), 6)
            self.assertEqual(calculator.result, 6)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(5, 5), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multipy(3, 3), 9)
        self.assertEqual(calculator.result, 9)

if __name__ == '__main__':
    unittest.main()