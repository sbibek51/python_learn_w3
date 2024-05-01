#format strings

#tomorrow Lists


'''the format method takes a passed argumants , formats them and    place
them in a strings where the  placeholders{} are
'''
age = 28
message ='My name is Bibek and my age is {}'
print(message.format(age))

quantity =3
item_no = 234
price = 350.0

shopping_list = 'I need {} item of Item no {} of price {} '
print(shopping_list.format(quantity,item_no,price))


a = 300
b = 55

if a > b:
    print('a is greater than b')
    print('a={} and b={}'.format(a,b))
else:
    print('b is greater than a')
    print('a={} and b={}'.format(a,b))

print(10+5)