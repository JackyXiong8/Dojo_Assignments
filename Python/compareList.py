list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','milk']
x = 0
for loop in range(len(list_one)):
    if list_one[loop] == list_two[loop]:
        x += 1
if x == len(list_one):
        print ("The lists are the same")
elif x != len(list_one):
        print ("The lists are not the same")

        
 
