def merge(nums1, m, nums2, n):
    p1, p2, p_write = m-1, n -1,(m+n) -1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p_write] = nums1[p1]
            p1-=1
        else:
            nums1[p_write] = nums2[p2]
            p2-=1
        p_write -=1
    return nums1 

nums1 = [1,2,3,0,0,0]
nums2 = [2, 5, 6]

print(merge(nums1, 3, nums2, 3))
