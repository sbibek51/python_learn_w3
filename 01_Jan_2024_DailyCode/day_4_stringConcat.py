#string concatination
a = 'Hello'
b = 'World'

c = a+' '+b

print(c)


age = '28'
message = 'my name is Bibek and my age is:' + age
print(message)

quantity = 3
item_no = 115
price = 50.0

statement = 'I want {} item of price {} for quantity of {}'
print(statement.format(item_no,price,quantity))