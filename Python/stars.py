



x = ["Tom", 1, "Michael", 5, 7, "Jimmy Smith"]


def draw_stars(arr):
    for loop in arr:  
        if type(loop) == str:
            print (loop[0] * len(loop))
        elif type(loop) == int:
            print ("*" * loop)

draw_stars(x)


