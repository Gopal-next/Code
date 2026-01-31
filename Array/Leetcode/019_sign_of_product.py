def sign_product(nums):
    prod = 1
    for i in range(len(nums)):
        prod *= nums[i]
    if prod>0:
        return 1
    elif prod < 0:
        return -1
    else:
        return 0
    
print(sign_product([-1,-2,-3,-4,3,2,1]))