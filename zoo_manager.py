# zoo manager classes
class Animal(): 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f'Animal makes this sound'
    
class Mammal(Animal):
    def __init__(self):
        super().__init__(self, species='Mammal')

    def give_birth(self):
        print(f'{self.name} has given birth')

class Bird(Animal):
    def __init__(self, wingspan):
        super().__init__(self, species='Bird', wingspan=0)
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self):
        super().__init__(self, species='Reptile')

    def bask_in_sun(self):
        print(f'{self.name} is basking in the sun.')

class Primate(Mammal):
    def __init__(self):
        super().__init__(self)

    def climb_trees(self):
        print(f'{self.name} is climbing trees.')

class Marsupial(Mammal):
    def __init__(self):
        super().__init__(self)

    def carry_baby(self):
        print(f"{self.name} is carrying it's baby.")

class Aviary():
    def __init__(self, birds):
        self.birds = Bird() # stores a list of bird instances

class ReptileEnclosure():
    def __init__(self, reptiles):
        self.reptiles = Reptile() # stores a list of reptile instances
        