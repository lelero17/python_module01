#!/usr/bin/python3


class Plant:
    """Represent a plant with basic attributes."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with his attributes.

        Args:
            name: Name of the Plant.
            height: height of the Plant.
            age: age of the Plant.
        """
        self._name = name
        self._height = 0.0
        self._age_in_days = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> float:
        """Return the plant's height."""
        return (self._height)

    def get_age(self) -> int:
        """Return the plant's age."""
        return (self._age_in_days)

    def set_height(self, new_height: float) -> str:
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

    def set_age(self, new_age: int) -> str:
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

    def grow(self) -> None:
        """Increase plant height by 0.8cm."""
        self._height += 0.8
        self._height = round(self._height, 1)

    def age(self) -> None:
        """Increase plant age by 1 day."""
        self._age_in_days += 1

    def show(self) -> None:
        """Return plant information in factory format."""
        print(f"{self._name}: {self._height}cm, {self._age_in_days} days old")


class Flower(Plant):
    """Represent a flower with color and blooming capability."""
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
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

    def show(self) -> None:
        """Return flower information in factory format."""
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        """Make the flower bloom."""
        self.has_bloomed = True


class Tree(Plant):
    """Represent a tree with trunk diameter and shade production."""
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        """Initialize a Tree with his attributes

        Args:
            name: Name of the Tree.
            height: height of the Tree.
            age: age of the Tree
            trunk_diameter: the width of the tree's stem
        """
        super().__init__(name, height, age)
        self.trunk_dia = trunk_diameter

    def show(self) -> None:
        """Return tree information in factory format."""
        super().show()
        print(f" Trunk diameter: {self.trunk_dia}cm")

    def produce_shade(self) -> None:
        """Make the tree produce a shade."""
        print(f"Tree {self._name} now produces a shade of "
              f"{self._height}cm long and {self.trunk_dia}cm wide.")


class Vegetable(Plant):
    """Represent a vegetable with harvest season and nutritional value."""
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: float) -> None:
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

    def show(self) -> None:
        """Return plant information in factory format."""
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def age(self) -> None:
        """Increase plant age by 1 day."""
        super().age()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types === \n=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)
    flower.show()
    flower.bloom()
    flower.show()
    print("\n=== Tree")
    tree.show()
    tree.produce_shade()
    print("\n=== Vegetable")
    vegetable.show()
    for i in range(1, 21):
        vegetable.grow()
        vegetable.age()
    vegetable.show()
