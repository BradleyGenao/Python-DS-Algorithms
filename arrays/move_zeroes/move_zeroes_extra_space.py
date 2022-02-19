def move_zeroes(array):
    zeroes = []
    non_zeroes = []
    for ele in array:
        if ele == 0:
            zeroes.append(ele)
        else:
            non_zeroes.append(ele)
    array[:] = non_zeroes + zeroes
    return array

array = [1,0,0,0,2,7,0,10,22]
print(move_zeroes(array))
