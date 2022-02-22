from collections import Counter
def majority_element(nums):
    counter = Counter(nums)
    maj_count = max(counter.values())
    for num in nums:
        if counter[num] == maj_count:
            return num
arr1 = [3, 2, 3]
arr2 = [2,2,1,1,1,2,2]
print("The majority element in array {} is {}".format(arr1, majority_element(arr1)))
print("The majority element in array {} is {}".format(arr2, majority_element(arr2)))
