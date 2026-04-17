import unittest

class MathDojo:
    """
    A simple MathDojo class that supports addition and subtraction.
    The methods return 'self' to allow for method chaining.
    """
    def __init__(self):
        # Initialize the result to 0
        self.result = 0

    def add(self, num, *nums):
        """
        Calculates the sum of num and all nums and adds it to the result.
        """
        self.result += num + sum(nums)
        return self

    def subtract(self, num, *nums):
        """
        Calculates the sum of num and all nums and subtracts it from the result.
        """
        self.result -= (num + sum(nums))
        return self

class MathDojoTests(unittest.TestCase):
    """
    Unit tests for the MathDojo class to ensure arithmetic operations
    and method chaining work as expected.
    """
    def setUp(self):
        # Create a fresh MathDojo instance before each test
        self.md = MathDojo()

    def test_add_single(self):
        # Test adding a single number
        self.md.add(10)
        self.assertEqual(self.md.result, 10)

    def test_add_multiple(self):
        # Test adding multiple numbers at once
        self.md.add(5, 5, 5)
        self.assertEqual(self.md.result, 15)

    def test_subtract_single(self):
        # Test subtracting a single number
        self.md.subtract(10)
        self.assertEqual(self.md.result, -10)

    def test_subtract_multiple(self):
        # Test subtracting multiple numbers at once
        self.md.subtract(5, 5, 5)
        self.assertEqual(self.md.result, -15)

    def test_chaining(self):
        # Test complex method chaining: (0 + 2) + (2 + 5 + 1) - (3 + 2) = 5
        x = self.md.add(2).add(2, 5, 1).subtract(3, 2).result
        self.assertEqual(x, 5)

if __name__ == "__main__":
    unittest.main()
