# zoo manager classes
class Animal: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal sound"
    
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} the {self.species} has given birth"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species='Bird')
        self.wingspan = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        return f'{self.name} the {self.species} is basking in the sun'

class Primate(Mammal):
    def climb_trees(self):
        return f'{self.name} the {self.species} is climbing trees'

class Marsupial(Mammal):
    def carry_baby(self):
        return f"{self.name} the {self.species} is carrying its baby"

# class Aviary:
#     def __init__(self, birds):
#         self.birds = birds #Bird() stores a list of bird instances

# class ReptileEnclosure:
#     def __init__(self, reptiles):
#         self.reptiles = reptiles #Reptile() stores a list of reptile instances

class Aviary:
    def __init__(self):
        self.birds = []

    def add(self, bird):
        self.birds.append(bird)

class ReptileEnclosure:
    def __init__(self):
        self.reptiles = [] 
    
    def add(self, reptile):
        self.birds.append(reptile)
        
# toucanSam = Animal('sam', 'toucan')
# print(toucanSam.speak())

# mammal = Mammal("Giraffe", "Giraffa camelopardalis")
# mammal.give_birth()

# snake = Reptile('diamond', 'rattlesnake')
# snake.bask_in_sun()

# bird1 = Bird('birdie', 'cardinal', 4)
# print(bird1.name)

# enclosure1 = Aviary([bird1])
# print(enclosure1.birds[0].name)