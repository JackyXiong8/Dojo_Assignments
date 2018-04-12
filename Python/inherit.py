class human:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.arms = 2
        self.strength = 2
        self.speed = 2
    def showall(self):
        print (self.arms, "arms", self.speed, "speed", self.eyes,"eyes")

    
class warrior(human):
    def __init__(self):
        super().__init__()
        self.arms = 4

class assassin(human):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.eyes = 6

w = warrior()
w.showall()

a = assassin()
a.showall()


