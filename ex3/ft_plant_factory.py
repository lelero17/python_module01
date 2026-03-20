#!/usr/bin/python3


class Plant:
    """Represent a plant with basic attributes."""
    def __init__(self, name, height, age):
        """Initialize a plant with his attributes.

        Args:
            name: Name of the Plant.
            height: height of the Plant
            age: age of the Plant
        """
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase plant height by 0.8cm."""
        self.height += 0.8
        self.height = round(self.height, 1)

    def age_one_day(self):
        """Increase plant age by 1 day."""
        self.age += 1

    def show(self):
        """Return plant information in factory format."""
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    stock = [
        Plant("Rose", 28.0, 30),
        Plant("Tulip", 15.0, 24),
        Plant("Daisy", 7.0, 2),
        Plant("Sunflower", 73.0, 85),
        Plant("Lilly", 21.0, 48)
    ]
    print("=== Plant Factory Output ===")
    for plant in stock:
        print(f"Created: {plant.show()}")
