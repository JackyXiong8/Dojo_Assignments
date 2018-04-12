words = "It's thanksgiving day. It's my birthday,too!"

#find and replace
print (words.find("day"))
print (words.replace("day","month"))

#min max
x = [2,54,-2,7,12,98]

print (min(x))
print (max(x))

#first and last
y = ["hello",2,54,-2,7,12,98,"world"]

print (y[0])
print (y[(len(y)-1)])

#New List
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print(z)

a=z[:len(z)//2]
b=z[len(z)//2:]
print(a,b)

b.insert(0,a)
print(b)
