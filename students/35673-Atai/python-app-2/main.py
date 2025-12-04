# class Predator:
#     x = "dangerous"

# species_list = ["wolf", "tiger", "lion"]
# predators = {species: Predator().x for species in species_list}

# print(predators)

class Animal:
    def __init__(self, name, kind, dangerous=False):
        self.name = name
        self.kind = kind
        self.__dangerous = dangerous   

    def greet(self):
        print(f"I am a {self.name}. I am a {self.kind}.")

    def is_dangerous(self):
        return self.__dangerous

    def attack(self):
        if self.__dangerous:
            print(f"{self.name} attacks!")
        else:
            print(f"{self.name} is not dangerous.")


class Predator(Animal):
    def __init__(self, name):
        super().__init__(name, "predator", True)

    def greet(self):  
        print(f"{self.name} is a predator and is very dangerous.")

    def attack(self): 
        print(f"{self.name} hunts its prey!")


class Prey(Animal):
    def __init__(self, name):
        super().__init__(name, "prey", False)

    def greet(self):  
        print(f"{self.name} is a peaceful prey animal.")

    def attack(self):
        print(f"{self.name} does not attack. It runs away!")


wolf = Predator("Wolf")
cow = Prey("Cow")

wolf.greet()
wolf.attack()
print()
cow.greet()
cow.attack()





