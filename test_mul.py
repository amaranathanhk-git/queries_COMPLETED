import unittest

from myfile import multiply


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-3, -4), 12)

    def test_mixed_signs(self):
        self.assertEqual(multiply(-3, 4), -12)

    def test_zero(self):
        self.assertEqual(multiply(0, 99), 0)

    def test_floats(self):
        self.assertAlmostEqual(multiply(2.5, 0.4), 1.0)

    def test_identity(self):
        self.assertEqual(multiply(7, 1), 7)


if __name__ == "__main__":
    unittest.main()
