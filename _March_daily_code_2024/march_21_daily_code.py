# Bibek Shiwakoti
def int_to_roman(number):
    num= [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym= ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i =12
    while number:
        div=number//num[i]
        number = number % num[i]



        while div:
            print(sym[i],end='')
            div-= 1
        i -= 1
        



number =56
int_to_roman(number)

# control shift alt and L to format the code int the pycharm community IDE