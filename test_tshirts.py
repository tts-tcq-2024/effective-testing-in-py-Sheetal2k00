import unittest
from tshirts import get_tshirt_size

class TestTshirtSize(unittest.TestCase):
    def test_tshirt_size(self):
        self.assertEqual(get_tshirt_size(13), "S")
        self.assertEqual(get_tshirt_size(39), "M")
        self.assertEqual(get_tshirt_size(44), "XL")
        self.assertEqual(get_tshirt_size(46), "XXL")
        # Add tests for edge cases
        self.assertEqual(get_tshirt_size(38), "S")
        self.assertEqual(get_tshirt_size(42), "L")
        self.assertEqual(get_tshirt_size(45), "XL")
        # Test missing input
        self.assertEqual(get_tshirt_size(41), "L")

if __name__ == "__main__":
    unittest.main()
