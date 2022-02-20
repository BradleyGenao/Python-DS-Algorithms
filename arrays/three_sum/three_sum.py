


def three_sum(array):
    
    def two_sum(index):
        left = index + 1
        right = len(arr) -1
        while left < right:
            triplet = [arr[index], arr[left], arr[right]]
            if sum(triplet) < 0:
                left +=1
            elif sum(triplet) > 0:
                right -=1
            else:
                triplets.append(triplet)
                left +=1
                right -=1
                while left < right and arr[left] == arr[left-1]:
                    left +=1

    triplets = []
    array.sort()

    for i in range(len(array)):
        if array[i] > 0:
            break
        if i ==0 or array[i] != array[i-1]:
            two_sum(i)

    return triplets

arr = [-1,0,1,2,-1,-4]

print(three_sum(arr))
