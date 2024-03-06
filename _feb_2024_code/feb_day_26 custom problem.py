#Bibek Shiwakoti
#Daily Coding

#Q. write a programa to add a digits of a number unless sum is single digit eg. input: 59 ->5+9=14->1+4=5

def nuber_spliitter(num):
    while num>10:
        num = num //10 + num%10
        return num

num = nuber_spliitter(59)
sum = num//10 + num%10
print(sum)

# control shifr alt and L to format the code in the pycharm