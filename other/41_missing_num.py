def missing_num(nums):
    num = 1

    while num in nums:
        num += 1
    return num

nums = [3,4,-1,1]
print(missing_num(nums))