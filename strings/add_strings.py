def add_strings(string1, string2):
    p1, p2 = len(string1)-1, len(string2)-1
    carry = 0
    res = []
    while p1 >= 0 or p2 >=0:
        ord_char1 = ord(string1[p1]) - 48  if p1 >= 0 else 0
        ord_char2 = ord(string2[p2]) - 48  if p1 >= 0 else 0 
        value = ((ord_char1 + ord_char2 + carry)) % 10
        carry = (ord_char1 + ord_char2 + carry) // 10
        p1-=1
        p2-=1
        res.append(value)
    if carry:
        res.append(carry)
    
    return ''.join(str(num) for num in res[::-1])    

num1 = "245"
num2 = "143"
print("num1 = {} num2 = {} num1 + num2 = ".format(num1, num2))
print(add_strings(num1, num2))
