def merge_interval(nums):
    a = []
    for i in range(len(nums)):
        if nums


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_interval(intervals))
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

iintervals = [[1,4],[4,5]]
print(merge_interval(iintervals))
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

inntervals = [[4,7],[1,4]]
print(merge_interval(inntervals))
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.