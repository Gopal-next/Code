def rotate_array(nums,k):
    n = k%len(nums)

    return nums[-n:] + nums[:-n]

print(rotate_array([1,2,3,4,5,6,7], 3))
print(rotate_array([-1,-100,3,99], 2))

print(rotate_array([1,2],7))