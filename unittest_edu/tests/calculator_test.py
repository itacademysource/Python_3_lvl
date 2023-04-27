from unittest import TestCase, main

from calculator import calculate


class CalculatorTest(TestCase):
    duplicate_assertion = 'Выражение должно содержать только 2 целых числа и 1 знак'

    def test_plus(self):
        """Addition check

        :return:
        """
        self.assertEqual(calculate('2 + 3'), 5)

    def test_minus(self):
        """Subtraction check

        :return:
        """
        self.assertEqual(calculate('3 - 1'), 2)

    def test_multi(self):
        """Multiplication check

        :return:
        """
        self.assertEqual(calculate('4 * 4'), 16)

    def test_divide(self):
        """Division testing

        :return:
        """
        self.assertEqual(calculate('16 / 4'), 4.0)

    def test_no_sign(self):
        """Testing for the absence of arithmetic operators

        :return:
        """
        with self.assertRaises(ValueError) as ex:
            calculate('some text')
        self.assertEqual('Выражение должно содержать арифметический знак +-*/', ex.exception.args[0])

    def test_two_sign(self):
        """Testing two passed arithmetic operators

        :return:
        """
        with self.assertRaises(ValueError) as ex:
            calculate('2 + 2 + 2')
        self.assertEqual(self.duplicate_assertion, ex.exception.args[0])

    def test_many_sign(self):
        """Testing many arithmetic operators

        :return:
        """
        with self.assertRaises(ValueError) as ex:
            calculate('3 ** 8')
        self.assertEqual(self.duplicate_assertion, ex.exception.args[0])

    def test_no_ints(self):
        """Testing non-integers

        :return:
        """
        with self.assertRaises(ValueError) as ex:
            calculate('2.5 * 9')
        self.assertEqual(self.duplicate_assertion, ex.exception.args[0])

    def test_strings(self):
        """Testing operations on strings

        :return:
        """
        with self.assertRaises(ValueError) as ex:
            calculate('a*b')
        self.assertEqual(self.duplicate_assertion, ex.exception.args[0])


if __name__ == '__main__':
    main()
