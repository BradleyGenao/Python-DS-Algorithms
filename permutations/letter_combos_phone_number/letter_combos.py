def letter_combinations(digits):
    if len(digits) < 1:
        return []
    digit_map = {"2" : "abc" , "3" : "def" , "4" : "ghi" , "5" : "jkl" , "6" : "mno" , "7" : "pqrs" , "8" : "tuv" , "9" : "wxyz" }
    
    ans = []
    
    def permute(index, path):
        if index == len(digits):
            ans.append(path)
            return 
        new_combo = digit_map[digits[index]]
        for char in new_combo:
            permute(index+1, path + char) 

     
   
    permute(0, '')
    return ans

number = "23"
print(letter_combinations(number))
