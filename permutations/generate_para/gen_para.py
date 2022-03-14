def generate_parenthesis(n):
    ans = []
    
    def backtrack(open_idx, close_idx, path):
        if close_idx == n:
            ans.append(path)
            return 
        if open_idx < n:
            backtrack(open_idx+1, close_idx, path + '(')
        if close_idx < open_idx:
            backtrack(open_idx, close_idx + 1, path + ')')
         



    backtrack(0,0,'')
    return ans



print(generate_parenthesis(3))
print(generate_parenthesis(2))
print(generate_parenthesis(1))
