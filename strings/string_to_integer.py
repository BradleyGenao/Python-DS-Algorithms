def string_to_integer(s):
    str_list = s.split()
    if len(str_list) == 0:
        return 0
    str_num = str_list[0]
    sign = -1 if str_num[0] == '-' else +1
    start = 1 if str_num[0] in '+-' else 0
    limit = 0x80000000 if sign < 0 else 0x7fffffff
    num = 0
 
    for i in range(start, len(str_num)):
        if not str_num[i].isdigit():
            break
        ord_num = ord(str_num[i])
        num *=10
        num += ord_num - 48
        if num >= limit:
            num = limit
            break
    return sign * num  

string1 = "42"
string2 = "     -42"
string3 = "4193 with words"
print(string_to_integer(string1))
print(string_to_integer(string2))
print(string_to_integer(string3))  
