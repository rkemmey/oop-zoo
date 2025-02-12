# zoo manager classes
class Animal: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f'Animal makes this sound'
    
class Mammal(Animal):
    def give_birth(self):
        print(f'{self.name} has given birth')

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species='Bird')
        self.wingspan = wingspan

class Reptile(Animal):
    def bask_in_sun(self):
        print(f'{self.name} is basking in the sun.')

class Primate(Mammal):
    def climb_trees(self):
        print(f'{self.name} is climbing trees.')

class Marsupial(Mammal):
    def carry_baby(self):
        print(f"{self.name} is carrying it's baby.")

class Aviary:
    def __init__(self, birds):
        self.birds = birds #Bird() stores a list of bird instances

class ReptileEnclosure:
    def __init__(self, reptiles):
        self.reptiles = reptiles #Reptile() stores a list of reptile instances
        
toucanSam = Animal('sam', 'toucan')
print(toucanSam.speak())

snake = Reptile('diamond', 'rattlesnake')
snake.bask_in_sun()

bird1 = Bird('birdie', 'cardinal', 4)
print(bird1.name)

enclosure1 = Aviary([bird1])
print(enclosure1.birds[0].name)