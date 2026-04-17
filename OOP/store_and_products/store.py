from product import Product

class Store:
    """
    Manages a collection of products. Supported operations include adding, 
    selling, and adjusting prices for inflation or clearance.
    """
    def __init__(self, name):
        # Initialize store name and an empty list of products
        self.name = name
        self.products = []

    def add_product(self, new_product):
        """
        Adds a new product to the store's inventory.
        Returns 'self' to allow for method chaining.
        """
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        """
        Removes and displays info for the product at the specified index (id).
        Prints an error if the index is out of bounds.
        Returns 'self' to allow for method chaining.
        """
        if 0 <= id < len(self.products):
            sold_product = self.products.pop(id)
            print(f"Product Sold:")
            sold_product.print_info()
        else:
            print(f"Error: Product with ID {id} not found in {self.name}.")
        return self

    def inflation(self, percent_increase):
        """
        Increases the price of all products in the store by a given percentage.
        Returns 'self' to allow for method chaining.
        """
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        """
        Decreases the price of all products in a specific category by a given percentage.
        Returns 'self' to allow for method chaining.
        """
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

    def display_all(self):
        """
        Prints the current inventory of the store.
        """
        print(f"\nInventory for {self.name}:")
        if not self.products:
            print("Empty")
        for product in self.products:
            product.print_info()
        return self
