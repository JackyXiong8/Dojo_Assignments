x = "fire,fire,water,fire"
y = "5"
z= " "
name = "Jacky"
print (x.upper())

print (x.lower())

print (x.capitalize())

print (x.count("fire"))

print (x.find("water"))

print (x.index("water"))

print (x.split())

print (y.join(x))

print (x.replace(x,y))

print ("Hello, my name is {}".format(name))

abc = [0,1,2,3,11,4,5,1.5,3]

print (len(abc))

print (max(abc))

print (min(abc))

print (abc.index(11))

(abc.append(20))
print (abc)

age = "17"
if age >="18":
    print ("You're legal!")
if age == "19":
    print ("You're 19")
else:
    print ("You're too young")

money = "500,000"
if money < "1,000,000":
    print ("Youre rich!!")
else:
    print ("Sorry, not enough")

for lol in range(0,5):
    print(lol)

for dog in x:
    print(dog)

balance = 0
while balance < 20:
    print (balance)
    balance +=1

print (min(abc))
