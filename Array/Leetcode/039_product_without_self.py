# brrute force approach
# def product_array_without_self(nums):
#     n = len(nums)
#     ans = [0] * n

#     for i in range(n):
#         product = 1

#         for j in range(n):
#             if i == j:
#                 continue
#             product *= nums[j]

#         ans[i] = product

#     return ans

# optimization here

# def product_array_without_self(nums):
#     n = len(nums)
#     left = [1]*n
#     right = [1]*n
#     ans = [1]*n

#     for i in range(1,n):
#         left[i] = left[i-1]*nums[i-1]
#     for j in range(n-2, -1, -1):
#         right[j] = right[j+1]* nums[j+1]
    
#     for k in range(n):
#         ans[k] = left[k]* right[k]
#     return left, right, ans

def product_array_without_self(nums):
    n = len(nums)
    answer = [1] * n

    # Store left products in answer
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Multiply by right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

a = [1,2,3,4]
print(product_array_without_self(a))
# [24,12,8,6]
b = [-1,1,0,-3,3]
print(product_array_without_self(b))
