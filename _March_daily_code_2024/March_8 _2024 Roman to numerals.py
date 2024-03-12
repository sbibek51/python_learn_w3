#Bibek Shiwakoti


def roman_to_numerals(roman):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_value=0
    prev_value =0

    for i in reversed(roman):
        value = roman_values[i]
        if value<prev_value:
            final_value-=value
        else:
            final_value += value

        prev_value= value
    return final_value



print(roman_to_numerals('II'))
print(roman_to_numerals('IX'))

"""next: numerals to roman"""
