def remove_ele(nums, val):
    # l = 0
    # for i in range(len(nums)):
    #     if nums[i] != val:
    #         nums[l] = nums[i]
    #         l += 1
    # return l

    left, right = 0, len(nums)-1
    i =0
    while left <= right:
        if nums[left]  == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1
    return left


print(remove_ele([3,2,2,3],3))
print(remove_ele([0,1,2,2,3,0,4,2],2))