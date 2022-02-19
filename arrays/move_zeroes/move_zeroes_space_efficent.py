def move_zeroes(array):
    anchor = 0
    for i, ele in enumerate(array):
        if ele != 0:
            array[i], array[anchor] = array[anchor], array[i]
            anchor +=1
    return array

arr = [3, 0, 0, 6, 0, 8, 0, 9, 66] 
print(move_zeroes(arr))
