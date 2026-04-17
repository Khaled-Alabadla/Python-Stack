class Product:
    """
    Represents a product in the store with a name, price, and category.
    """
    def __init__(self, name, price, category):
        # Initialize product attributes
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        """
        Updates the product's price based on a percentage change.
        If is_increased is True, the price is increased.
        Otherwise, the price is decreased.
        Returns 'self' to allow for method chaining.
        """
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self

    def print_info(self):
        """
        Prints the product's details formatted for readability.
        Returns 'self' to allow for method chaining.
        """
        print(f"Product: {self.name} | Category: {self.category} | Price: ${self.price:.2f}")
        return self
