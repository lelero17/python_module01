#!/usr/bin/python3


class Plant:
    """Represent a plant with basic attributes."""
    def __init__(self, name: str, height: float, age: int) -> None:
        """Initialize a plant with his attributes.

        Args:
            name: Name of the Plant.
            height: height of the Plant
            age: age of the Plant
        """
        self.name = name
        self.height = height
        self.age_in_days = age

    def show(self) -> None:
        """Displays the plant information."""
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Tulip", 15.0, 20),
        Plant("Daisy", 5.0, 2)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
