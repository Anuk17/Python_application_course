import unittest

import papps as calculator


class DTestCalculator1(unittest.TestCase):
    def test_add_functionality1(self):
        result = calculator.calc_add(5, 7)
        self.assertEqual(result, 12)

    def test_add_functionality_of_two_negative_numbers2(self):
        result = calculator.calc_add(-18, -26)
        self.assertEqual(result, -44)


class CTestCalculator2(unittest.TestCase):

    @unittest.skip('Meri marzi')
    def test_sub_functionality3(self):
        result = calculator.calc_sub(7, 7)
        self.assertEqual(result, 0)

    def test_sub_functionality_of_two_negative_numbers4(self):
        result = calculator.calc_sub(-18, -26)
        self.assertEqual(result, 8)


class BTestCalculator3(unittest.TestCase):
    def test_mul_functionality5(self):
        result = calculator.calc_mul(5, 7)
        self.assertEqual(result, 35)

    def test_mul_functionality_of_two_negative_numbers6(self):
        result = calculator.calc_mul(-8, -6)
        self.assertEqual(result, 48)


class ATestCalculator4(unittest.TestCase):
    def test_mod_functionality7(self):
        result = calculator.calc_mod(4, 3)
        self.assertEqual(result, 5)

    def test_mod_functionality_of_two_negative_numbers8(self):
        result = calculator.calc_mod(-4, -3)
        self.assertEqual(result, 5)



