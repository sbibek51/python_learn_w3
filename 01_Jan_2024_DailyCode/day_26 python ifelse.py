#Bibek Shiwakoti
#today we are learning the ifelse in python
a = 33
b= 543
if a>b:
    print('a is greater than b...')
else:
    print('b is greater than a  ..')

#elif works as if provided condition is not working try this

a= 33
b= 33
if a > b:
    print('a is greater than b')
elif(a==b):
    print('a and b are equal')


# the else catches the anything which is not caght by the preceeding conditions
a= 300
b= 400
if a>b:
    print('a is greater than b')
elif(a==b):
    print('a and b are equal')
else:
    print('b is greater than b')


a = 33
b = 44
if not a > b:
    print('a is not greater than b')


# we can not have an if statement without content i.e. it can not be empty
# if we need so we need to write pass
a = 50
b = 60
if not a > b:
    pass


#tomorrow pytnon while loops