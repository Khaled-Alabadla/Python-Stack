# Store and Products Project

An object-oriented programming (OOP) assignment in Python that simulates a simple store management system. It demonstrates class association, method chaining, and complex logic for inventory and price management.

## Project Structure

- **`product.py`**: Defines the `Product` class with attributes for name, price, and category. It includes methods for updating prices and printing product information.
- **`store.py`**: Defines the `Store` class which manages a list of `Product` instances. It supports adding products, selling products (with error handling), and applying store-wide or category-specific price changes.
- **`run_store.py`**: A demonstration script that initializes a store, adds several products, and performs various operations to test the system's logic.

### Steps to Run

1.  **Navigate to the folder**:
    ```bash
    cd store_and_products
    ```

2.  **Execute the demonstration script**:
    ```bash
    python run_store.py
    ```

## Core Functionalities

### 1. Method Chaining
Most methods in the `Store` and `Product` classes return `self`, allowing for concise operations like:
```python
my_store.add_product(laptop).add_product(phone).display_all()
```

### 2. Price Management
- **Inflation**: Increase prices of all products in the store by a specific percentage.
- **Clearance**: Target specific categories for discounts, useful for seasonal sales or stock clearance.

### 3. Error Handling
The `sell_product` method includes validation to ensure the requested product ID (index) exists within the current inventory, preventing runtime crashes.
