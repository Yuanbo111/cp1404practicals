import random
from car import Car

class UnreliableCar(Car):
    """An unreliable car that sometimes doesn't drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, with reliability percentage."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its reliability."""
        if random.uniform(0, 100) < self.reliability:
            # Drive normally using the parent class method
            return super().drive(distance)
        else:
            # Car fails to drive
            return 0
