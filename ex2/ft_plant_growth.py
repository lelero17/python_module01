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

    def grow(self) -> None:
        """Increase plant height by 0.8cm."""
        self.height += 0.8
        self.height = round(self.height, 1)

    def age(self) -> None:
        """Increase plant age by 1 day."""
        self.age_in_days += 1

    def show(self) -> None:
        """Return current plant information"""
        print(f"{self.name}: {self.height}cm, {self.age_in_days} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30)
    initial_height = plant.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.show()
        plant.grow()
        plant.age()
    print(f"Growth this week: {round(plant.height - initial_height)}cm")
