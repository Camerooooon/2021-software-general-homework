class Fish:
    def __init__(self, name, color, species):
        self.name = name
        self.color = color
        self.species = species
        self.alive = True

    def bye_bye(self):
        self.alive = False

    def __repr__(self):
        return "><(((" + ("o" if self.alive else "*") + ">"

class MegaFish(Fish):
    def __init__(self, name, color, species):
        super().__init__(name, color, species)
        self.lives = 10

    def bye_bye(self):
        self.lives -= 1
        if self.lives == 0:
            self.alive = False

    def eat(self, fish: Fish):
        fish.bye_bye()
        print(f"yum I eat {fish.name}")


pet = Fish("Jimmy", "blue", "goldfish")

mega_pet = MegaFish("REEEE", "rainbow", "swordfish")
print(mega_pet.name)
print(mega_pet)
while mega_pet.alive:
    mega_pet.bye_bye()
print(mega_pet)

print(pet.name)
print(pet)
mega_pet.eat(pet)
print(pet)
