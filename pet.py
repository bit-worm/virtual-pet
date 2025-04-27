class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger == 0:
            print(f"{self.name} is full...")
        elif (self.hunger > 2) & (self.happiness < 10):
            print("Eating...")
            self.hunger -= 3
            self.happiness += 1
        else:
            print("Eating...")
            self.hunger = 0
            self.happiness = 10

    def sleep(self):
        print('Sleeping...')
        if self.energy < 6:
            self.energy += 5
        else:
            self.energy = 10

    def play(self):
        if self.energy == 0:
            print("Too tired...")
        elif (self.energy > 1) & (self.happiness < 9) & (self.hunger < 10):
            print('Playing...')
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        else:
            print('Playing...')
            self.energy = 0
            self.happiness = 10
            self.hunger = 10

    def train(self, trick):
        print('Training...')
        self.tricks.append(trick)

    def show_tricks(self):
        print('I can do these...')
        for trick in self.tricks:
            print(trick)

    def get_status(self):
        print(f"Name: {self.name}\nHappiness: {self.happiness}\nEnergy: {self.energy}\nHunger: {self.hunger}")
