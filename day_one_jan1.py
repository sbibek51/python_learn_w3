#Today is Janauary 1 of 2024
a = int(input('Enter number between 1 and 100 inclusive:'))
if a < 1 or a > 100:
    print('Given number is out of range')
    exit()
else:
    print('all numbers less than given numbers between one and hundred is:')
    for i in range(1, a):
      print(i)