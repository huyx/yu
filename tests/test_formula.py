import textwrap
import unittest

from yu.formula import Formula, FormulaError


class FormulaTest(unittest.TestCase):
    def test_valid_formula(self):
        formula = Formula('a=1')
        formula({})

    def test_invalid_formula(self):
        with self.assertRaises(FormulaError):
            formula = Formula('print(if 1)')
            formula({})

    def test_context(self):
        formula = Formula(textwrap.dedent('''
            pi = 3.1415926
            周长 = 2 * 半径 * pi
            面积 = pi * 半径 * 半径
        '''), '圆周长与面积')
        context = {
            '半径': 3,
        }
        formula(context)
        self.assertIn('半径', context)
        self.assertIn('周长', context)
        self.assertIn('面积', context)


if __name__ == '__main__':
    unittest.main(verbosity=3)
