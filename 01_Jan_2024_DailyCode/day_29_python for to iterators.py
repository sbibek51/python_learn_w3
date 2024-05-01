# it is possible to define a increament value in for loops
for i in range(2,21,2):
    print(i)
    # this is printing the even numbers from 2 to 20

#Else in for loop
# else block in for loop specifies that the value to be printed when the loop finishes
for i in range (21):
    print(i)
else:
    print('finally loop finishes')

# the else statement is not executed if the loop is stopped by the break statement
for x in range (6):
    if (x==4):
        break #pass
    print(x)
else:
    print('finally printed all the values successfully')


#nested loops
#the inner loop will run one time for each value of outer loop

adjectives =['red','big','tasty']
fruits = ['apple','cherry', 'berry']

for x in adjectives:
    for y in fruits:
        print(x,y)


#for loop cannot be empty but for some reason if we need for loop with content
# we need to put the pass statement
for x in [0,1,2]:
    pass


# tomorrow python functions