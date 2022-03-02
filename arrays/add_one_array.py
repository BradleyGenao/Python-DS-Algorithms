def plus_one(digits):
    n = len(digits)
    for i in reversed(range(n)):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] +=1
            return digits
    return [1] + digits

arr1 = [1, 2, 4]
arr2 = [9]
arr3 = [9,9,9,9]
arr4 = [4,3,6,8,9]

print("Adding One to the following arrays {} | {} | {} | {}".format(arr1, arr2, arr3, arr4))
print("Results = {} | {} | {} | {}".format(plus_one(arr1), plus_one(arr2), plus_one(arr3), plus_one(arr4)))
