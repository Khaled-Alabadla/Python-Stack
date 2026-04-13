import unittest

def reverseList(arr):
    pass

def isPalindrome(word):
    pass

def coins(cents):
    pass

def factorial(n):
    pass

def fibonacci(n):
    pass

class TDDAssignmentTests(unittest.TestCase):
    
    # Tests for reverseList
    def testReverseList(self):
        # Given case
        arr1 = [1, 3, 5]
        reverseList(arr1)
        self.assertEqual(arr1, [5, 3, 1])
        
        # Test Case 2: Even length
        arr2 = [2, 4, 6, 8]
        reverseList(arr2)
        self.assertEqual(arr2, [8, 6, 4, 2])
        
        # Test Case 3: Empty list
        arr3 = []
        reverseList(arr3)
        self.assertEqual(arr3, [])
        
        # Test Case 4: Single element
        arr4 = [42]
        reverseList(arr4)
        self.assertEqual(arr4, [42])

        # Test Case 5: Strings (just to be sure)
        arr5 = ["a", "b", "c"]
        reverseList(arr5)
        self.assertEqual(arr5, ["c", "b", "a"])

    # Tests for isPalindrome
    def testIsPalindrome(self):
        # Given cases
        self.assertTrue(isPalindrome("racecar"))
        self.assertFalse(isPalindrome("rabcr"))
        
        # Test Case 3: Simple palindrome
        self.assertTrue(isPalindrome("mom"))
        # Test Case 4: Not a palindrome
        self.assertFalse(isPalindrome("hello"))
        # Test Case 5: Empty string
        self.assertTrue(isPalindrome(""))
        # Test Case 6: Single character
        self.assertTrue(isPalindrome("a"))
        # Test Case 7: Case sensitivity (Assuming exact match)
        self.assertFalse(isPalindrome("Racecar"))
        # Test Case 8: Palindrome with spaces
        self.assertTrue(isPalindrome("amanaplanacanalpanama"))

    # Tests for coins
    def testCoins(self):
        # Given case
        self.assertEqual(coins(87), [3, 1, 0, 2])
        
        # Test Case 2: Zero cents
        self.assertEqual(coins(0), [0, 0, 0, 0])
        # Test Case 3: One of each (25 + 10 + 5 + 1 = 41)
        self.assertEqual(coins(41), [1, 1, 1, 1])
        # Test Case 4: Only pennies
        self.assertEqual(coins(4), [0, 0, 0, 4])

    # Tests for factorial
    def testFactorial(self):
        # Given case
        self.assertEqual(factorial(5), 120)
        
        # Test Case 2: Factorial of 0
        self.assertEqual(factorial(0), 1)
        # Test Case 3: Factorial of 1
        self.assertEqual(factorial(1), 1)
        # Test Case 4: Factorial of 4
        self.assertEqual(factorial(4), 24)

    # Tests for fibonacci
    def testFibonacci(self):
        # Given cases
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(4), 3)
        
        # Test Case 3: fib(0)
        self.assertEqual(fibonacci(0), 0)
        # Test Case 4: fib(1)
        self.assertEqual(fibonacci(1), 1)
        # Test Case 5: fib(6)
        self.assertEqual(fibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()
