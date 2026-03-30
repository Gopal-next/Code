def max_subarray(nums):
    # Kadane's algorithm
    max_sum = current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


    # max_sum = float('-inf')
    # current_sum = 0
    # for n in nums:
    #     current_sum += n
    #     max_sum = max(max_sum, current_sum)
    #     if current_sum < 0:
    #         current_sum = 0
    # return max_sum

# Example usage:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))  # Output: 6 (subarray [4,-1,2,1])

nums = [1]
print(max_subarray(nums))  # Output: 1 (subarray [1])

nums = [5,4,-1,7,8]
print(max_subarray(nums))  # Output: 23 (subarray [5,4,-1,7,8])