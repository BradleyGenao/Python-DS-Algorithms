def roman_to_int(string):
    
    roman_map = {  "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000,  "IV": 4, "IX" : 9, "XL": 40, "XC": 90, "CD" : 400,  "CM": 900 }
    index = 0
    ans = 0
    
    while index < len(string):
        if index < len(string) -1 and string[index:index+2] in roman_map:
            ans += roman_map[string[index:index+2]]
            index+=2
        else:
            ans += roman_map[string[index]]
            index+=1
    return ans
    
string1 = "III"
string2 = "LVIII"
string3 = "MCMXCIV"
print(roman_to_int(string1))
print(roman_to_int(string2))
print(roman_to_int(string3))

