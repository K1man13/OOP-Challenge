from pet import Pet

# Create a pet instance
my_pet = Pet("Lion")

# Test the pet's functionality
my_pet.get_status()

# Test eating
my_pet.eat()
my_pet.get_status()

# Test playing
my_pet.play()
my_pet.get_status()

# Test sleeping
my_pet.sleep()
my_pet.get_status()

# Test training and showing tricks
my_pet.train("Roar")
my_pet.train("Pounce")
my_pet.train("Roar")  # Try teaching a trick it already knows
my_pet.show_tricks()

# Test playing when energy is low
my_pet.energy = 1  # Manually set low energy for testing
my_pet.play()
my_pet.get_status()