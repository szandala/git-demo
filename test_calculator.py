import unittest
from calculator import add, subtract, multiply, divide, split_by_operators, make_operation

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Arrange
        numbers = [5, 7]
        expected = 12
        # Act
        received = add(*numbers)
        # Assert
        self.assertEqual(received, expected)

    def test_divide(self):
        # Arrange
        numbers = [2, 3]
        expected = 0.666
        # Act
        received = divide(*numbers)
        # Assert
        self.assertEqual(received, expected)

if __name__ == '__main__':
    unittest.main()
