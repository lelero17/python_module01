#!/usr/bin/python3


class Plant:
    """Represent a plant with basic attributes."""
    def __init__(self, name, height, age):
        """Initialize a plant with his attributes.

        Args:
            name: Name of the Plant.
            height: height of the Plant.
            age: age of the Plant.
        """
        self._name = name
        self._height = 0
        self._age_in_days = 0
        self.set_height(height)
        self.set_age(age)
        self._stats = Plant.Stats()

    def get_height(self):
        """Return the plant's height."""
        return (self._height)

    def get_age(self):
        """Return the plant's age."""
        return (self._age_in_days)

    def set_height(self, new_height):
        """Set the plant's height with validation.

        Args:
            new_height: New height value (must be >= 0).
        """
        if new_height < 0:
            return (f"{self._name}: Error, height can't be negative\n"
                    f"Height update rejected")
        else:
            self._height = new_height
            return (f"Height updated: {round(self._height)}cm")

    def set_age(self, new_age):
        """Set the plant's age with validation.

        Args:
            new_age: New age value (must be >= 0).
        """
        if new_age < 0:
            return (f"{self._name}: Error, age can't be negative\n"
                    f"Age update rejected")
        else:
            self._age_in_days = new_age
            return (f"Age updated: {self._age_in_days} days")

    def grow(self):
        """Increase plant height by 0.8cm."""
        self._height += 0.8
        self._height = round(self._height, 1)
        self._stats._grow_count += 1

    def age(self):
        """Increase plant age by 1 day."""
        self._age_in_days += 1
        self._stats._age_count += 1

    def show(self):
        """Return plant information in factory format."""
        print(f"{self._name}: {self._height}cm, {self._age_in_days} days old")
        self._stats._show_count += 1
        
    
    @staticmethod 
    def is_older_than_year(age):
        """Check if age is older than an year."""
        return age > 365
    
    @classmethod
    def create_anonymous(cls):
        """"Creates an anonymous plant with default values"""
        return cls("Unknown plant", 0.0, 0)
        
    class Stats:
        """Track statistical data from a plant."""
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0
        
        def display(self):
            """Display the statistics"""
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")
            


class Flower(Plant):
    """Represent a flower with color and blooming capability."""
    def __init__(self, name, height, age, color):
        """Initialize a Flower with his attributes

        Args:
            name: Name of the Flower.
            height: height of the Flower.
            age: age of the Flower.
            color: color of the Flower
        """
        super().__init__(name, height, age)
        
        self.color = color
        self.has_bloomed = False

    def show(self):
        """Return flower information in factory format."""
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self):
        """Make the flower bloom."""
        self.has_bloomed = True
        

class Tree(Plant):
    """Represent a tree with trunk diameter and shade production."""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize a Tree with his attributes
        
        Args:
            name: Name of the Tree.
            height: height of the Tree.
            age: age of the Tree
            trunk_diameter: the width of the tree's stem
        """
        super().__init__(name, height, age)
        self.trunk_dia = trunk_diameter
        self.shade = False
        self._stats = Tree.Stats()
        
    def show(self):
        """Return tree information in factory format."""
        super().show()
        print(f" Trunk diameter: {self.trunk_dia}cm") 
            
    def produce_shade(self):
        """Make the tree produce a shade."""
        self._stats._shade_count += 1
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_dia}cm wide.")
    
    class Stats(Plant.Stats):
        """Track statistical data for a tree."""
        def __init__(self):
            super().__init__()
            self._shade_count = 0
        
        def display(self):
            super().display()
            print(f" {self._shade_count} shade")


class Vegetable(Plant):
    """Represent a vegetable with harvest season and nutritional value."""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize a Vegetable with his attributes
        
        Args:
            name: Name of the Vegetable.
            height: height of the Vegetable.
            age: age of the Vegetable.
            harvest_season: the time when to collect the vegetable.
            nutritional_value: Initial nutritional value of the vegetable.
        """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        """Return plant information in factory format."""
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")
    
    def age(self):
        """Increase plant age by 1 day."""
        super().age()
        self.nutritional_value += 1


class Seed(Flower):
    """Represent the Seeds of the flowers when the Flower has bloomed."""
    def __init__(self, name, height, age, color, num_seeds):
        """Initialize the Seed class with his attributes
        
        Args:
            has_bloomed: true if the Flower has bloomed, else false"
        """
        super().__init__(name, height, age, color)
        self.num_seeds = num_seeds
        
    def show(self):
        """Show if and how many seeds the Flower has"""
        super().show()
        print(f" Seeds: {self.num_seeds if self.has_bloomed else 0}")
        
def display_stats(plant):
    """Display statistics for any kind of plant"""
    plant._stats.display()

if __name__ == "__main__":
    seed = Seed("Sunflower", 80.0, 45, "yellow", 42)
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print("=== Garden statistics ===\n=== Check year-old")
    
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}\n")
    
    print("=== Flower")
    flower.show()
    display_stats(flower)
    flower.grow()
    flower.bloom()
    flower.show()
    display_stats(flower)
    print()
    
    print("=== Tree")
    tree.show()
    display_stats(tree)
    tree.produce_shade()
    display_stats(tree)
    print()
    
    print("=== Seed")
    seed.show()
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    display_stats(seed)
    
    print("\n=== Anonymous")
    anonym = Plant.create_anonymous()
    anonym.show()
    display_stats(anonym)