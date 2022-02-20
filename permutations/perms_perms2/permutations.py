def permute(array):
    ans = []

    def permute_rec(arr, path):
        if len(arr) == 0:
            ans.append(path)
            return 
        for i in range(len(arr)):
            permute_rec(arr[i+1:] + arr[:i], path + [arr[i]]) 

    permute_rec(array, [])
    return ans

array1 = [1, 2, 3]
array2 = [0, 1]
array3= [1]

print(permute(array1))
print(permute(array2))
print(permute(array3))

