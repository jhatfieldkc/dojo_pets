class Pet:

    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        print(self.energy)
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy is", self.energy)
        print(f"{self.name}'s health is", self.health)
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        if self.type == "dog":
            print(f"{self.name} says WOOF!")
        elif self.type == "cat":
            print(f"{self.name} says MEEEEOOOWWW")
        elif self.type == "monkey":
            print(f"{self.name} just farted")
        return self