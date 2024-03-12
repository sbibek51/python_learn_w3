#Bibek Shiwakoti

# program to convert from a integers to roman


def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print(sym[i], end="")
            div -= 1
        i -= 1



number = 9
print("Roman value is:", end = " ")
printRoman(number)



"""https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/"""
# control shift alt and L to format a code in the pycharm IDE