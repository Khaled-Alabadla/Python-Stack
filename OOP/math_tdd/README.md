# Math and TDD Assignments

This directory contains Python assignments focusing on object-oriented programming (OOP) principles, method chaining, and Test-Driven Development (TDD).

## Project Structure

- **`math_dojo.py`**: Implements a `MathDojo` class that demonstrates method chaining for addition and subtraction.
- **`tdd_assignment.py`**: A collection of utility functions (reversing lists, palindrome checks, coin calculation, factorial, and fibonacci) with comprehensive unit tests for each.
- **`tdd_math_dojo.py`**: Applies TDD principles to the `MathDojo` class using the `unittest` framework to verify its functionality.

### Steps to Run

1.  **Navigate to the folder**:
    ```bash
    cd math_tdd
    ```

2.  **Run Math Dojo**:
    This script runs several test cases and prints the results to the console.
    ```bash
    python math_dojo.py
    ```

3.  **Run TDD Assignment Tests**:
    This script uses the `unittest` module to run multiple test cases for various utility functions.
    ```bash
    python tdd_assignment.py
    ```

4.  **Run TDD Math Dojo Tests**:
    This script specifically tests the `MathDojo` implementation using `unittest`.
    ```bash
    python tdd_math_dojo.py
    ```

## Key Concepts Demonstrated
- **Method Chaining**: Allowing multiple method calls on a single object instance in a single line.
- **Variable Arguments (`*args`)**: Handling an arbitrary number of inputs in functions.
- **Unit Testing**: Using the `unittest` library to automate the verification of code logic.
- **Recursion**: Implementing mathematical sequences like Factorial and Fibonacci.
