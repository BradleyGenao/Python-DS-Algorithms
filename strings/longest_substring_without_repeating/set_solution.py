def length_of_longest_substring(string):
    start, ans = 0, 1
    substring = set()
   
    for end, char in enumerate(string):
        while char in substring:
            substring.remove(string[start])
            start +=1
        substring.add(char)
        ans = max(ans, end - start + 1)
    return ans

string = "tyyyhshfocnna"
print(length_of_longest_substring(string))      
