def  rotate_array(nums, k):
    first = nums[len(nums)-k:]
    last = nums[:len(nums)-k]
    return first + last

nums = [-1,-100,3,99]
k = 2

print(rotate_array(nums,k))