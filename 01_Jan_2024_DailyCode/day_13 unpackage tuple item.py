#day 13
#unpackage tuple item
fruits = ('apple','cherry','banana','mango')
print(fruits)
for i in fruits:
    print(i)
    print('\n')

(green, yellow, white, orange) =fruits
print(green)
print(yellow)
print(white)
print(orange)

(green, yellow, *white) =fruits
print(green)
print(yellow)
print(white)


