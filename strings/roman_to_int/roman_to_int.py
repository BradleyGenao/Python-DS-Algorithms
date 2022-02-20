def roman_to_integer(string):
    
    roman_map = { 'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    ans = 0
    index = 0
    
    while index < len(string):
        if index+1 < len(string) and roman_map[string[index]] < roman_map[string[index+1]]:
            ans += roman_map[string[index+1]] - roman_map[string[index]]
            index+=2
        else:
            ans += roman_map[string[index]]
            index +=1
    return ans 

string1 = 'III'
string2 = 'LVIII' 
string3 = 'MCMXCIV'

print(roman_to_integer(string1)) 
print(roman_to_integer(string2)) 
print(roman_to_integer(string3)) 
