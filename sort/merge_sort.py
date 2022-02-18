class MergeSort():
    
    def __init__(self, arr=[4,3,1,4,2], size=5):
         self.arr = arr
         self.size = size
    
    def print(self):
         for i, num in enumerate(self.arr):
              print("Index: {} Element: {}".format(i, num))
    
def merge_sort(arr):
    if len(arr) == 1:
        return arr 
        
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
        
    left_part = merge_sort(left)
    right_part = merge_sort(right)
    return merge(left_part,right_part)
     
def merge(left, right):
     i = j = 0
     ans = []
     while i < len(left) and j < len(right):
         if left[i] < right[j]:
             ans.append(left[i])
             i+=1
         else:
             ans.append(right[j])
             j +=1
     ans += left[i:]
     ans += right[j:]
     return ans
test = [4,3,1,5,2]
print(test)
print('*******************Merge Sort******************')
sorted_arr = merge_sort(test)
print(sorted_arr)
