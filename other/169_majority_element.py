nums = [2,2,1,1,1,2,2,1,1,3,3,3,3,3,3,3,3,3,3]

### brute force 

# for i in range(len(nums)):
#     count = 0

#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#             count += 1
#     if count > len(nums) //2:
#         print(nums[i])
#         break

def majority_elements(nums):
    candidate = None
    count = 0

    for num in nums:
        if count ==0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

nums = [6,5,5]
print(majority_elements(nums))