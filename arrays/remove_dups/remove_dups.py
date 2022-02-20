def remove_dups(arr):
    anchor = 1
    for i in range(len(arr)-1):
        if array[i] != arr[i+1]:
            arr[anchor] = arr[i+1]
            anchor +=1
    
    return arr
array = [11,11,12,20,20,25,27,66,66,87,99,99]
print("Original Array = {}".format(array))
print("New Array = {} ".format(remove_dups(array)))
