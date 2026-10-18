def product_of_array(nums):
    # res = []
    # for i in range(len(nums)):
    #     p = 1
    #     for j in range(len(nums)):
    #         if i != j :
    #             p = p* nums[j]
    #     res.append(p)
    # return res

    # n = len(nums)
    # prefix = [1]*n
    # suffix = [1]*n

    # for i in range(len(nums)-1):
    #     prefix[i+1] = prefix[i] * nums[i]

    # for j in range(len(nums)-1,0,-1):
    #     suffix[j-1] = suffix[j]* nums[j]

    # res = []
    # for i in range(len(nums)):
    #     res.append(prefix[i]*suffix[i])
    # return res
    n = len(nums)
    res = [1]*n

    for i in range(1,len(nums)):
        res[i] = res[i-1]*nums[i-1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]

    return res
    pass
nums = [1,2,3,4]
print(product_of_array(nums))