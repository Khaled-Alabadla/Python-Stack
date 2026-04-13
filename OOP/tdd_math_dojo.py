import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + sum(nums)
        return self

    def subtract(self, num, *nums):
        self.result -= (num + sum(nums))
        return self

class MathDojoTests(unittest.TestCase):
    def setUp(self):
        self.md = MathDojo()

    def test_add_single(self):
        self.md.add(10)
        self.assertEqual(self.md.result, 10)

    def test_add_multiple(self):
        self.md.add(5, 5, 5)
        self.assertEqual(self.md.result, 15)

    def test_subtract_single(self):
        self.md.subtract(10)
        self.assertEqual(self.md.result, -10)

    def test_subtract_multiple(self):
        self.md.subtract(5, 5, 5)
        self.assertEqual(self.md.result, -15)

    def test_chaining(self):
        x = self.md.add(2).add(2, 5, 1).subtract(3, 2).result
        self.assertEqual(x, 5)

if __name__ == "__main__":
    unittest.main()
