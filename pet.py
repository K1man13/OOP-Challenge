class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # Starting energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting happiness level (0-10)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Reduce hunger by 3, not below 0
        self.happiness = min(10, self.happiness + 1)  # Increase happiness by 1, not above 10
        print(f"{self.name} ate some food! Hunger decreased, happiness increased.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Increase energy by 5, not above 10
        print(f"{self.name} took a nap! Energy increased.")

    def play(self):
        if self.energy >= 2:  # Check if pet has enough energy to play
            self.energy -= 2  # Decrease energy by 2
            self.happiness = min(10, self.happiness + 2)  # Increase happiness by 2, not above 10
            self.hunger = min(10, self.hunger + 1)  # Increase hunger by 1, not above 10
            print(f"{self.name} had fun playing! Happiness increased, energy decreased, hunger increased.")
        else:
            print(f"{self.name} is too tired to play!")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)  # Add new trick to the list
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name}'s tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")