# Base class: Vehicle
class Vehicle:
    def move(self):
        pass  

# Car class inherits from Vehicle and implements the move method
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle and implements the move method
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class inherits from Vehicle and implements the move method
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Function to demonstrate polymorphism
def make_move(vehicle):
    vehicle.move()

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism by calling the same method on different objects
make_move(car)  # Output: Driving 🚗
make_move(plane)  # Output: Flying ✈️
make_move(boat)  # Output: Sailing ⛵
