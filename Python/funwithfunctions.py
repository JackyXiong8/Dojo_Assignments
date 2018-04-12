

#odd even

def oddeven():
    for num in range(1,2000):
        if num % 2 == 0:
            print ("number is ",(num),"This number is even")
        elif num % 2 != 0:
            print ("number is ",(num),"This number is odd")
oddeven()

#Multiplication argument

a = [2,4,10,16]
x = []
def multiply(a):
    for product in range(len(a)):
        a[product] = a[product] * 2
        x.append(a[product])
    print (x)
multiply(a)



