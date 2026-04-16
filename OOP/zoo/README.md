# Zoo Assignment

A simple Python project to manage animals in a zoo using Object-Oriented Programming (OOP) principles.

## Features
- **Animal Classes**: Base `Animal` class with specific subclasses for `Lion`, `Tiger`, and `Bear`.
- **Zoo Management**: A `Zoo` class to manage multiple animal instances.
- **Feeding System**: Update health and happiness of animals individually or collectively.

## Implementation Steps
To build this system, I followed these key steps:
1. **Base Class Creation**: Developed the `Animal` class to handle common attributes like `name`, `age`, `health`, and `happiness`.
2. **Specialization**: Created subclasses (`Lion`, `Tiger`, `Bear`) that inherit from `Animal`, each with unique attributes and custom `feed()` behaviors.
3. **Zoo Management**: Implemented the `Zoo` class to store animal instances and perform group actions like `feed_all()`.
4. **Method Chaining**: Added `return self` to methods to allow for expressive, single-line commands.

## Output Screenshot
![User Assignment Terminal Output](/output.png)

## Setup & Execution
1. Ensure Python is installed.
2. Run the script:
   ```bash
   python zoo.py
   ```
