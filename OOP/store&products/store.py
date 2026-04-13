from product import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        if 0 <= id < len(self.products):
            sold_product = self.products.pop(id)
            sold_product.print_info()
        else:
            print(f"Error: Product with ID {id} not found in {self.name}.")
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self

    def display_all(self):
        print(f"\nInventory for {self.name}:")
        if not self.products:
            print("Empty")
        for product in self.products:
            product.print_info()
        return self
