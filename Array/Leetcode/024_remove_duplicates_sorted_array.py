def remove_dup(nums):
    # k = 1
    # for j in range(1,len(nums)):
    #     if nums[j] != nums[j-1]:
    #         nums[k] = nums[j]
    #         print(nums[k])
    #         print(nums[j])
    #         print(nums)
    #         k = k+1
    # return k 


    left , right = 1, len(nums)
    i =0
    while left < right:
        if nums[left] !=nums[i]:
            i += 1
            nums[left], nums[i] = nums[i], nums[left]
        left += 1
    return i+1

print(remove_dup([1,1,2]))
print(remove_dup([0,0,1,1,1,2,2,3,3,4]))