# Base class: Superhero
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        print(f"I am {self.name} from the {self.universe} universe!")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}! 💥")

# Subclass: Villain (inherits from Superhero)
class Villain(Superhero):
    def __init__(self, name, power, universe, evil_plan):
        super().__init__(name, power, universe)
        self.evil_plan = evil_plan

    # Override use_power to show polymorphism
    def use_power(self):
        print(f"{self.name} unleashes chaos with {self.power}! 😈")
        print(f"Beware! Evil plan: {self.evil_plan}")

# Create superhero instance
hero = Superhero("Photon Girl", "Light Manipulation", "NovaVerse")
hero.introduce()
hero.use_power()

print()  # For spacing

# Create villain instance
villain = Villain("Dark Phantom", "Shadow Control", "NovaVerse", "Plunge the world into eternal darkness")
villain.introduce()
villain.use_power()
