
# Part 1
greeting = "hello"
name = "dojo"

print (greeting,name)

# Part 2

arr = ['Wish', 'Mop', 'Bleet', 'March', 'Jerk']

for loop in arr:
    print (loop)

# Part 3

def multiply(num):
    x = [ ]
    for i in range(1,25):
        num = num * 2
    x.append(num)
    print (x)

multiply(40)

# part 4

def reverseString(string):
    
    newstring = string[::-1]

    print (newstring)

reverseString("Jacky")

# Part 5

x = 10
x = x * 7
y = 30
z = y + x
z = z * 3
z = z - y
z = z / 27
x = z + y
y = 3
x = x + y
print (x,y,z)
if x % 10 == 0:
    print ("True")
else:
    print ("False")



