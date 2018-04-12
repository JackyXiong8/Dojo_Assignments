inputVar = [1,2,3,4,"fire","water"]

strcount = 0
intcount = 0
strValues = ""
intValues = 0

for loop in inputVar:
    if type(loop) == str:
        strcount += 1
        strValues += loop
    if type(loop) == int:
        intcount += 1
        intValues += loop
if strcount > 1 and intcount < 1:
    print ("The list you entered is of string type")
if strcount < 1 and intcount > 1:
    print ("The list you entered is of integer type")
elif strcount > 1 and intcount > 1:
    print ("The list you entered is mixed")
        

print(strcount)
print(intcount)
print (strValues)
print (intValues)
