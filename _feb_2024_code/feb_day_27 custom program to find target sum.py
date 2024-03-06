#Bibek Shiwakoti
#Program to find four numbers from array whose sum is target sum
list_1 = [1, 0, -1, 0, -2, 2, 10, 11]
target_sum = 0
list_2 = []

print('Given list is:', list_1)
print('Length of this list is:', len(list_1))

for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        for k in range(j + 1, len(list_1)):
            for l in range(k + 1, len(list_1)):
                current_sum = list_1[i] + list_1[j] + list_1[k] + list_1[l]

                if current_sum == target_sum:
                    list_2.append([list_1[i], list_1[j], list_1[k], list_1[l]])

print('subset of 4  list items that sums to 0 are:', list_2)


#Control shift alt and L to format the code in pycharm