name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def roster(list1, list2):
    new_dict = list(zip(list1, list2))
    new_dict = dict(new_dict)
    print (new_dict)

roster(name, favorite_animal)

