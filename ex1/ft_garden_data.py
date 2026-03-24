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

    def show(self):
        """Displays the plant information."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Tulip", 15, 20),
        Plant("Daisy", 5, 2)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
