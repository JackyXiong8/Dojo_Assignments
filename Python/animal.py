



class Animals:
    def __init__(self):
        self.health = 10
        self.name ="pandora"

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health += 5
        return self
    def hp(self):
        print (self.health)

class Dog(Animals):
    def __init__(self):
        super().__init__()
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animals):
    def __init__(self):
        super().__init__()
        self.health = 170
    def fly(self):
        self.health -= 10
        return self

class Cat(Animals):
    def __init__(self):
        super().__init__()
        self.health = 5
    def claw(self):
        self.health -= 1
        return self


a = Dog()

d = Dragon()

c = Cat()

d.health

