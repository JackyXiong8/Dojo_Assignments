
import random


def grades():
    for loop in range(1,11):
        x = random.randint(60, 100)
        if x > 59 and x < 70:
            print ("Score:",x,"; Your grade is D")
        if x > 69 and x < 80:
            print ("Score:",x,"; Your grade is C")
        if x > 79 and x < 90:
            print ("Score:",x,"; Your grade is B")
        if x > 89:
            print ("Score:",x,"; Your grade is A")

grades()