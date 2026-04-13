from store import Store
from product import Product

# 1. Create a store
my_store = Store("Khaled Store")

# 2. Create some products
laptop = Product("MacBook Pro", 2500.00, "Electronics")
phone = Product("iPhone 15", 1000.00, "Electronics")
headphones = Product("AirPods Max", 550.00, "Audio")
coffee = Product("Premium Roast", 15.00, "Grocery")

# 3. Add products to store
print(f"Adding products to {my_store.name}...")
my_store.add_product(laptop).add_product(phone).add_product(headphones).add_product(coffee)

# 4. Display initial inventory
my_store.display_all()

# 5. Test Sell Product
my_store.sell_product(1)

# Display current inventory
my_store.display_all()

# 6. Test Inflation (10% increase across all products)
my_store.inflation(0.10)
my_store.display_all()

# 7. Test Clearance (20% discount on 'Audio' category)
my_store.set_clearance("Audio", 0.20)
my_store.display_all()
