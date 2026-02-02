def square_of_sorted(nums):
    # li = []
    # for i in range(len(nums)):
    #     li.append(nums[i]*nums[i])
    # return sorted(li)

    # two pointer technique
    res = [0] * len(nums)
    left , right = 0, len(nums) -1
    pos = len(nums) -1

    while left <= right:
        left_s = nums[left]*nums[left]
        right_s = nums[right]*nums[right]

        if left_s > right_s:
            res[pos] = left_s
            left += 1
        else:
            res[pos] = right_s
            right -= 1
        pos -= 1
    return res

print(square_of_sorted([-4,-1,0,3,10]))
print(square_of_sorted([-7,-3,2,3,11]))