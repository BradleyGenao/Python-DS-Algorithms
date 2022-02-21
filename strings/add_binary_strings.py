def add_binary(string1, string2):
    x, y = int(string1, 2), int(string2, 2)
    while y:
        value = x ^ y
        carry = (x&y) << 1
        x, y = value, carry
    return bin(x)[2:]

a = "1010"
b = "1011"
print("{} + {} = ".format(a, b))
print(add_binary(a, b))
