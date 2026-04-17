import unittest

def reverseList(arr):
    """
    Reverses an array in-place using a two-pointer approach.
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def isPalindrome(word):
    """
    Checks if a string is a palindrome (reads the same forward and backward).
    Note: This is case-sensitive and includes spaces.
    """
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


def coins(cents):
    """
    Calculates the minimum number of coins (quarters, dimes, nickels, pennies)
    needed to represent a given amount of cents.
    """
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return [quarters, dimes, nickels, pennies]


def factorial(n):
    """
    Calculates the factorial of a number 'n' using recursion.
    n! = n * (n-1) * ... * 1
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Calculates the nth Fibonacci number using recursion.
    F(n) = F(n-1) + F(n-2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


class TDDAssignmentTests(unittest.TestCase):
    """
    A collection of unit tests to verify the correctness of the utility functions.
    """
    
    # Tests for reverseList function
    def testReverseList(self):
        # Case 1: Standard odd-length list
        arr1 = [1, 3, 5]
        reverseList(arr1)
        self.assertEqual(arr1, [5, 3, 1])
        
        # Case 2: Standard even-length list
        arr2 = [2, 4, 6, 8]
        reverseList(arr2)
        self.assertEqual(arr2, [8, 6, 4, 2])
        
        # Case 3: Empty list
        arr3 = []
        reverseList(arr3)
        self.assertEqual(arr3, [])
        
        # Case 4: Single element list
        arr4 = [42]
        reverseList(arr4)
        self.assertEqual(arr4, [42])

        # Case 5: List of strings
        arr5 = ["a", "b", "c"]
        reverseList(arr5)
        self.assertEqual(arr5, ["c", "b", "a"])

    # Tests for isPalindrome function
    def testIsPalindrome(self):
        # Case 1: Standard palindrome
        self.assertTrue(isPalindrome("racecar"))
        # Case 2: Non-palindrome
        self.assertFalse(isPalindrome("rabcr"))
        # Case 3: Short palindrome
        self.assertTrue(isPalindrome("mom"))
        # Case 4: Standard word
        self.assertFalse(isPalindrome("hello"))
        # Case 5: Empty string (is considered symmetric)
        self.assertTrue(isPalindrome(""))
        # Case 6: Single character
        self.assertTrue(isPalindrome("a"))
        # Case 7: Case sensitivity check
        self.assertFalse(isPalindrome("Racecar"))
        # Case 8: Long palindrome
        self.assertTrue(isPalindrome("amanaplanacanalpanama"))

    # Tests for coins function
    def testCoins(self):
        # Case 1: Given example 87c -> 3Q, 1D, 0N, 2P
        self.assertEqual(coins(87), [3, 1, 0, 2])
        
        # Case 2: Zero cents
        self.assertEqual(coins(0), [0, 0, 0, 0])
        # Case 3: One of each coin type
        self.assertEqual(coins(41), [1, 1, 1, 1])
        # Case 4: Only pennies
        self.assertEqual(coins(4), [0, 0, 0, 4])

    # Tests for factorial function
    def testFactorial(self):
        # Case 1: 5! = 120
        self.assertEqual(factorial(5), 120)
        
        # Case 2: 0! = 1
        self.assertEqual(factorial(0), 1)
        # Case 3: 1! = 1
        self.assertEqual(factorial(1), 1)
        # Case 4: 4! = 24
        self.assertEqual(factorial(4), 24)

    # Tests for fibonacci function
    def testFibonacci(self):
        # Case 1: F(5) = 5
        self.assertEqual(fibonacci(5), 5)
        # Case 2: F(4) = 3
        self.assertEqual(fibonacci(4), 3)
        
        # Case 3: F(0) = 0
        self.assertEqual(fibonacci(0), 0)
        # Case 4: F(1) = 1
        self.assertEqual(fibonacci(1), 1)
        # Case 5: F(6) = 8
        self.assertEqual(fibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()
