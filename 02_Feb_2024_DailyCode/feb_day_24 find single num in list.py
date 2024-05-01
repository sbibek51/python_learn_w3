# Bibek Shiwakoti
# Day 24 February 2024
"""write program to find a number in a list that doesnot occur twice
eg. [1,1,2,2,3,4,4]
output: 3
"""

my_list =[1,1,2,2,3,4,4]

my_dictionary ={}

for i in my_list:
    my_dictionary[i] =my_dictionary.get(i,0)+1


single_count = [i for key,value in my_dictionary.items() if value == 1]

print(my_dictionary)
print(single_count)



#print reverse of given words
given_words = 'hello world'
splitted_words = given_words.split()
print(splitted_words)
rev =splitted_words[::-1]
print(rev)
string_joined = ' '.join(splitted_words)
print(string_joined)
