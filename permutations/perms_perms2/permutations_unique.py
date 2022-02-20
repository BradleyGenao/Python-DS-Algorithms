def permute(array):
    ans = []
    array.sort()
     
    def permute_rec(arr, path):
        if len(arr) == 0:
            ans.append(path)
            return 
        for i in range(len(arr)):
            if i == 0 or arr[i] != arr[i-1]:
                permute_rec(arr[i+1:] + arr[:i], path + [arr[i]])

    permute_rec(array, [])
    return ans 



array1 = [1,1,2]
array2 = [1, 2, 3]
print(permute(array1))
print(permute(array2))   
