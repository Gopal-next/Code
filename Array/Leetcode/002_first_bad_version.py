def isBadVersion(k):
    pass


def firstBadVersion(n):
    left , right = 1, n
    while left< right:
        mid = (left + right) //2
        if isBadVersion(mid):
            right =mid
        else:
            left = mid +1
    return left


    # def searchRange(nums, target):
    # first = last = -1

    # for i, n in enumerate(nums):
    #     if n == target:
    #         if first == -1:
    #             first = i
    #         last = i

    # return [first, last]
