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
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self):
        """Return the plant's height."""
        return (self._height)

    def get_age(self):
        """Return the plant's age."""
        return (self._age)

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
            self._age = new_age
            return (f"Age updated: {self._age} days")

    def grow(self):
        """Increase plant height by 0.8cm."""
        self._height += 0.8
        self._height = round(self._height, 1)

    def age_one_day(self):
        """Increase plant age by 1 day."""
        self._age += 1

    def show(self):
        """Return plant information in factory format."""
        return (f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    plant = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.show()}\n")
    print(plant.set_height(25.0))
    print(plant.set_age(30))
    print()
    print(plant.set_height(-1))
    print(plant.set_age(-1))
    print(f"\nCurrent state: {plant.show()}")
