def length_of_longest_substring(string):
    start = 0
    substring = []
    ans = 1
    for end, char in enumerate(string):
        while char in substring:
            substring.remove(string[start])
            start +=1
        substring.append(char)
        ans = max(ans, end - start + 1)
    return ans

string = "pwwkew"
print(length_of_longest_substring(string))
