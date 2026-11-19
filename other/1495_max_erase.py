def max_erase(nums):
    a = []
    for i in range(len(nums)):
        if nums[i] not in a:
            a.append(nums[i])
    return sum(a)
    # pass

nums = [5,2,1,2,5,2,1,2,5]
print(max_erase(nums))