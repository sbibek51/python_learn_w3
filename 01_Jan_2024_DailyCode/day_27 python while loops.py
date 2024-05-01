# today we are going to learn a while loops in python
# pass statement
a = 40
b = 30
if a > b:
     print('a is greater than b')
else:
     pass
# if statement can not be empty but by anychance if we need to keep empty we need to write pass


# python has two primitive loops
# for loops and while loops



i =1
while i<=10:
    print(i)
    i=i+1
# remember to continue a while loop otherwise while loop will run in infinite loop

# with break statent we can stoop the while loop even if the condition is true
i = 1
while i<=10:
    print('\n')
    print(i)
    if (i == 3):
        break

    i+=1  #this will give only 1,2 and 3 as output


# with the continue statement we can stop the iteration and continue to next iteration
i = 1
while i<=10:
    print('\n')
    i+=1
    if (i == 3):
        continue
    print(i)


# we can use else in while loop as well which will be printed when condition is no longer meet

i = 1
while(i<10):
    print(i)
    i+=1
    if(i==2):
        continue
    print(i)
else:
    print('i is now greater than ten')

