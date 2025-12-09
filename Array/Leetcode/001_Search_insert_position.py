def search(nums, target):
    left, right = 0, len(nums) -1
    while left <= right:
        mid = (left+ right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

    # for i, num in enumerate(nums):
    #     if num >= target:
    #         return i
    # return len(nums)
nums = [1,3,5,6]
target = 6
print(search(nums, target))

# https://www.geeksforgeeks.org/dsa/binary-search/

