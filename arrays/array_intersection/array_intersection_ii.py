from collections import Counter
def intersection(array_one, array_two):
    if not array_one or not array_two:
        return []
    counter = Counter(array_one)
    ans = []
    for ele in array_two:
        if counter[ele]:
            counter[ele] -=1
            ans.append(ele)
    return ans

nums1, nums2 = [1,2,2,1], [2, 2]
nums3, nums4 = [4,9,5], [9,4,9,8,4]
nums5, nums6 = [7,6,3,5,7,2,1], [2, 8, 3, 5]
print("The intersection of {} and {} = {}".format(nums1, nums2, intersection(nums1, nums2)))
print("The intersection of {} and {} = {}".format(nums3, nums4, intersection(nums3, nums4)))
print("The intersection of {} and {} = {}".format(nums5, nums6, intersection(nums5, nums6)))
            
