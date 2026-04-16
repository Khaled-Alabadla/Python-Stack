# Parent class for all animals
class Animal:
    def __init__(self, name, age, health=50, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    # Display status of the animal
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")
        return self

    # Feed the animal to increase its health and happiness
    def feed(self):
        self.health += 10
        self.happiness += 10
        return self


# Subclass for Lion
class Lion(Animal):
    def __init__(self, name, age, pride_size=5):
        # Lions start with specific health and happiness
        super().__init__(name, age, health=60, happiness=40)
        self.pride_size = pride_size # Unique attribute

    # Lions get a bigger happiness boost when fed
    def feed(self):
        self.health += 10
        self.happiness += 20
        return self

    # Show lion-specific information
    def display_info(self):
        super().display_info()
        print(f"  Lion Unique Info - Pride Size: {self.pride_size}")
        return self


# Subclass for Tigers
class Tiger(Animal):
    def __init__(self, name, age, stripe_count=100):
        # Tigers start with high health
        super().__init__(name, age, health=70, happiness=30)
        self.stripe_count = stripe_count # Unique attribute

    # Tigers get a large health boost when fed
    def feed(self):
        self.health += 25
        self.happiness += 5
        return self

    # Show tiger-specific information
    def display_info(self):
        super().display_info()
        print(f"  Tiger Unique Info - Stripe Count: {self.stripe_count}")
        return self


# Subclass for Bears
class Bear(Animal):
    def __init__(self, name, age, favorite_food="Fish"):
        # Bears start with highest starting health
        super().__init__(name, age, health=80, happiness=20)
        self.favorite_food = favorite_food # Unique attribute

    # Bears get a balanced boost when fed
    def feed(self):
        self.health += 15
        self.happiness += 15
        return self

    # Show bear-specific information
    def display_info(self):
        super().display_info()
        print(f"  Bear Unique Info - Favorite Food: {self.favorite_food}")
        return self


# Class to manage the collection of animals
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    # Add an animal instance to the zoo
    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            print("Only Animal instances can be added to the zoo.")
        return self

    # Print information for all animals in the zoo
    def print_all_info(self):
        print("\n" + "="*20, f"WELCOME TO {self.name.upper()}", "="*20)
        for animal in self.animals:
            animal.display_info()
        print("="*65 + "\n")
        return self

    # Command to feed every animal in the zoo
    def feed_all(self):
        print(f"Feeding all animals in {self.name}...")
        for animal in self.animals:
            animal.feed()
        return self

if __name__ == "__main__":
    my_zoo = Zoo("Central Park")

    # Creating specific animal instances
    nala = Lion("Nala", 5, pride_size=12)
    simba = Lion("Simba", 4)
    rajah = Tiger("Rajah", 3, stripe_count=105)
    baloo = Bear("Baloo", 10, favorite_food="Honey")

    my_zoo.add_animal(nala).add_animal(simba).add_animal(rajah).add_animal(baloo)

    # Display initial state
    print("Initial Zoo Status:")
    my_zoo.print_all_info()

    # Feeding specific animals
    print("Feeding Nala and Rajah specifically...")
    nala.feed()
    rajah.feed()

    # Feeding all animales
    my_zoo.feed_all()

    # Final status check
    my_zoo.print_all_info()
