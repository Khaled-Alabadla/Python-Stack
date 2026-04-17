from store import Store
from product import Product

# Initialize the store
my_store = Store("Khaled Store")

# Define initial products
laptop = Product("MacBook Pro", 2500.00, "Electronics")
phone = Product("iPhone 15", 1000.00, "Electronics")
headphones = Product("AirPods Max", 550.00, "Audio")
coffee = Product("Premium Roast", 15.00, "Grocery")

# Add products to the store using method chaining
print(f"Adding products to {my_store.name}...")
my_store.add_product(laptop).add_product(phone).add_product(headphones).add_product(coffee)

# Show the inventory before any modifications
my_store.display_all()

# Test Case: Sell a product (ID 1 is the iPhone)
print("\n--- Selling Product at Index 1 ---")
my_store.sell_product(1)

# Review inventory after sale
my_store.display_all()

# Test Case: Apply inflation (10% increase to all remaining products)
print("\n--- Applying 10% Inflation ---")
my_store.inflation(0.10)
my_store.display_all()

# Test Case: Category Clearance (20% discount on 'Audio' category)
print("\n--- Applying 20% Clearance on 'Audio' ---")
my_store.set_clearance("Audio", 0.20)
my_store.display_all()
