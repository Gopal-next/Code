
def intersection(nums1, nums2):
        # Brute Force Approach
        # For each element in nums1:
        #   - Check if it exists in nums2 → O(n)
        #   - Check if already in result → O(n)
        #   - Remove from nums2 → O(n)
        # Overall Time: O(n^2) (nested linear operations)
        # Space: O(n) for result

    res = []
    for i in range(len(nums1)):
        if nums1[i] in nums2 and nums1[i] not in res:
            res.append(nums1[i])
            nums2.remove(nums1[i])
    return res



def intersection(nums1, nums2):
        # Optimized with one set
        # Store nums2 in set → O(m)
        # Iterate nums1 and check membership → O(1)
        # Time: O(n + m)
        # Space: O(m) (better than full set approach)

    nums2_set = set(nums2)
    res = set()

    for num in nums1:
        if num in nums2_set:
            res.add(num)

    return list(res)


# Approach: Hashing (Set Intersection)

# Idea:
# - Use set for O(1) lookup
# - Intersection removes duplicates automatically

# Time: O(n + m)
# Space: O(n + m)

# 🔁 Pattern: "Common elements" → think SET / HASHING first
# 🔁 Follow-up: If duplicates allowed → use frequency map (dict)
# 🔁 Alternative: If arrays sorted → use Two Pointers (O(1) space)
# 🔁 Watch: Avoid list 'in' and remove() → O(n) each (TLE risk)

# Edge Cases:
# - Empty arrays
# - All elements same
# - No intersection