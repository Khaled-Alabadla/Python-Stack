# Chaining Assignment

A simple Python project demonstrating the concept of **Method Chaining** by returning `self` from object methods.

## Concept
Method chaining allows you to call multiple methods on the same object in a single line of code. This is achieved by having each method `return self` at the end of its execution.

## Example Usage
```python
user.make_deposit(100).make_deposit(200).make_withdrawal(50)
```

## How to Run
1. Ensure Python is installed.
2. Run the script:
   ```bash
   python chaining.py
   ```
