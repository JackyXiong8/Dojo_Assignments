

import random

toss = random.randint(1,2)

print (toss)
def cointoss():
    heads = 0
    tails = 0
    total = 0
    for loop in range(1,5001):
        coin = random.randint(1,2)
        if coin == 1:
            heads = heads + 1
            total += 1
            print ("Attempt #",total,": Throwing a coin... It's a head! Got",heads,"head(s) so far and",tails,"tail(s) so far")
        if coin == 2:
            tails += 1
            total += 1
            print ("Attempt #",total,": Throwing a coin... It's a tail! Got",tails,"tail(s) so far and",heads,"head(s) so far")

cointoss()

