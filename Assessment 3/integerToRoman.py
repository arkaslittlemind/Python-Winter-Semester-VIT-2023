def intToRoman(num):
    roman_mapping = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
    
    roman_numeral = ""
    
    for value, symbol in roman_mapping.items():
        while num >= value:
            roman_numeral += symbol
            num -= value
    
    return roman_numeral

# Test cases
input_num_1 = 9
output_1 = intToRoman(input_num_1)
print(output_1)  # Output: "IX"

input_num_2 = 58
output_2 = intToRoman(input_num_2)
print(output_2)  # Output: "LVIII"
