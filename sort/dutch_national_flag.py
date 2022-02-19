def sort(array):
    red, white, blue = 0, 0, len(array) - 1 
    while white <= blue:
        if array[white] == 0:
            array[white], array[red] = array[red], array[white]
            white +=1
            red +=1
        elif array[white] == 1:
            white +=1
        else:
            array[blue], array[white] = array[white], array[blue]
            blue-=1
    return array

test = [2,1,0,0,1,2,1,0,1]
print(sort(test))
