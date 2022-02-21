from collections import defaultdict
def longest_substring(string, k):
    start = 0
    ans = 0
    substring = defaultdict(int) 

    for end, char in enumerate(string):
        substring[char] +=1
        
        while len(substring) > k:
            substring[string[start]] -=1
            if substring[string[start]] == 0:
                del substring[string[start]]
            start +=1
        ans = max(ans, end - start + 1)
    return ans 

s1 = "eceba"
s2 = "aa"

print("Longest Substring with 2 distinct chars {} = {}".format(s1, longest_substring(s1, 2))) 
print("Longest Substring with 1 distinct char {} = {}".format(s2, longest_substring(s2, 1))) 
