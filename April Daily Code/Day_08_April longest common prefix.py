# Bibek Shiwakoti


def longest_common_prefix(given_list):
    if not given_list:
        return ''
    else:
        given_list.sort()   #imp
        prefix = given_list[0]
        for i in range(1,len(given_list)):
            for j in range (len(prefix)):
                if prefix[j] != given_list[i][j]:
                    prefix = prefix[:j]
                    break
        return prefix



str_list = ["flower", "flow", "flight"]
print("Longest common prefix:", longest_common_prefix(str_list))


# control shift alt and L to format a code in the pycharm