def left_right_sum(nums):
    result = []
    for i in range(len(nums)):
        leftSum = 0
        rightSum = 0
        for j in range(i):
            leftSum += nums[j]
        for j in range(i+1, len(nums)):
            rightSum += nums[j]
        result.append(abs(leftSum-rightSum))
    return result

print(left_right_sum(nums = [10,4,8,3]))

