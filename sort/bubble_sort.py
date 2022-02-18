class BubbleSort:
    def __init__(self, arr = [3,4,2,1,5] ):
        self.arr = arr    
        self.size = len(arr)
       
    def print_array(self):
        for index, num in enumerate(self.arr):
            print("Index: {} Element: {}".format(index, num))
    
    def sort(self):
        for _ in range(self.size):
            for i in range(self.size - 1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
        return self.arr 
            


test = BubbleSort([4,3,1,2])
sorted_array = BubbleSort(test.arr)
test.print_array()
print("***********Bubble Sort****************")
sorted_array.sort()
sorted_array.print_array()
