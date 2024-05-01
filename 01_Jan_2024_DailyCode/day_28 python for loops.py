#for loops in python is used for iterating over string, loops ,tuple or dictionaries
# in other words for loops is used to iterate over a sequence in python
# using for loops we can execute a statement  once for each items
fruits =['apple','banana','cherry','strawberry']
for i in fruits:
    print(i)
    if i == 'banana':
        break


# the for loops does not require an indexing variable to set beforehead
for x in 'banana':
    print(x)

mobiles = ['apple','samsung', 'redmi']
for i in mobiles:
    if i == 'samsung':
        break
    print(i)


print('use of continue is to continue iterate leaving teh current point')

mobiles = ['apple','samsung', 'redmi']
for i in mobiles:
    if i == 'samsung':
        continue
    print(i)



# the range function in the python
# the range function returns a value starting by 0 by default

for i in range(6):
    print(i)


for i in range(0,6):
    print(i)

print('************************')
for x in range (5,16):
   print(x)

# It is possible to define a increament value
