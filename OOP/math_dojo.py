class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# Create an instance
md = MathDojo()

# Test cases
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(f"Result after provided test: {x}")

# Additional tests for 'add'
md.result = 0 
print("\nTesting 'add' method:")
md.add(10)
print(f"After add(10): {md.result}")
md.add(5, 5, 5)
print(f"After add(5, 5, 5): {md.result}")
md.add(1, 2, 3, 4, 5)
print(f"After add(1, 2, 3, 4, 5): {md.result}")

# Additional tests for 'subtract'
md.result = 100 
print("\nTesting 'subtract' method:")
md.subtract(20)
print(f"After subtract(20): {md.result}")
md.subtract(10, 10, 10)
print(f"After subtract(10, 10, 10): {md.result}")
md.subtract(5, 4, 3, 2, 1)
print(f"After subtract(5, 4, 3, 2, 1): {md.result}")

# Final chaining test
md.result = 0
final_val = md.add(100).subtract(50, 20).add(10, 5).subtract(5).result
print(f"\nFinal chaining test result: {final_val}")
