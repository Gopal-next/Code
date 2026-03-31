def number_of_good_pair(nums):
    seen = {}
    count = 0 
    for i in range(len(nums)):
        if nums[i] in seen:
            count += seen[nums[i]]
            seen[nums[i]] += 1
        else:
            seen[nums[i]] = 1
    
    return count


nums = [1,2,3,1,1,3]
print(number_of_good_pair(nums))

nums1 = [1,1,1,1]
print(number_of_good_pair(nums1))

nums2 = [1,2,3]
print(number_of_good_pair(nums2))