#odds
for odds in range(0,1000):
    if odds % 2 != 0:
        print (odds)


#divisible by 5

for fives in range(5,1000000):
    if fives % 5 == 0:   
        print (fives) 


#sum

a = [1, 2, 5, 10, 255, 3]

b = sum(a)
print (b)

#average

a = [1, 2, 5, 10, 255, 3]

b = sum(a)

c = b / len(a)

print (c)