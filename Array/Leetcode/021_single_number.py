# def single_number(nums):
#     """
#     Given a non-empty array of integers nums, every element appears twice except for one. 
#     Find that single one.

#     Args:
#     nums (List[int]): List of integers where every element appears twice except for one.

#     Returns:
#     int: The single number that appears only once.
#     """
#     result = 0
#     for num in nums:
#         result ^= num
#     return result

# other approach using set
def single_number(nums):
    """
    Given a non-empty array of integers nums, every element appears twice except for one. 
    Find that single one.

    Args:
    nums (List[int]): List of integers where every element appears twice except for one.

    Returns:
    int: The single number that appears only once.
    """
    seen = set()
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    return seen.pop() if seen else 0
# Example usage:
nums = [4,1,2,1,2]
print(single_number(nums))  # Output: 4