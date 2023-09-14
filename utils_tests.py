import unittest
from utils import Utils

class UtilsTests(unittest.TestCase):

    def setUp(self):
        self.utilsInstance = Utils()

    def test_reversed(self):
        self.assertEqual(self.utilsInstance.reversed(123), 321)
    
    def test_reversed_with_float(self):
        with self.assertRaises(ValueError):
            self.utilsInstance.reversed(4.2)

    def test_reversed_with_string(self):
        with self.assertRaises(ValueError):
            self.utilsInstance.reversed('nothing')

    def test_formatter(self):
        binary, octal = self.utilsInstance.formatter(37)
        self.assertEqual(binary, '0b100101')
        self.assertEqual(octal, '0o45')

    def test_formatter_with_float(self):
        with self.assertRaises(ValueError):
            self.utilsInstance.formatter(3.5)
    
    def test_formatter_with_string(self):
        with self.assertRaises(ValueError):
            self.utilsInstance.formatter('problem')

if __name__ == "__main__":
    unittest.main()
