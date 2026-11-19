
# first = [[1, 3], [2, 6]]
# second = [[2, 6]]

# start = min(first[0][0], first[1][0])
# print(first[0][0]) # 1
# print(first[0][1]) # 3
# print(first[1][0]) # 2
# print(first[1][1]) # 6

# # Find the larger ending number
# end = max(first[1][0], first[1][1])
# print(end)

# # Combine start and end
# merged = [start, end]

# print(merged)


# intervals = [[4,7],[1,4]]

# merged = [intervals[0]]
# print("merge ", merged)
# for interval in intervals[1:]:
#     last = merged[-1]

#     # Check whether the current interval overlaps
#     if interval[0] <= last[1]:
#         # Update the ending number of last
#         last[1] = max(last[1], interval[1])
#         print("innn ", interval[0])
#         print(last)
#         print("last ",last[1])
#         # pass
#     else:
#         # If they do not overlap, add interval
#         merged.append(interval)
#         # pass

# print(merged)
from collections import Counter

# #409 longest palindrome
# s = "bb"
# countt = Counter(s)
# print(countt)
# sum = 0
# maxx = float('-inf')
# for key, value in countt.items():
#     if value % 2 == 0:
#         sum += value
#     else:
#         sum += value - 1
#         maxx = max(maxx, 1)
# print(sum)


# 451. Sort Characters By Frequency

# s = "tree"

# count = Counter(s)
# print(count)

# for key, value in count.items():
#     print(key, value)

# ops = ["5","2","C","D","+"]

# # a = '-6'
# # print(a.lstrip('-').isdigit())
# def diagonal(mat):
#     summ = 0
#     for i in range(len(mat)):
#         summ += mat[i][i]
#         summ += mat[i][len(mat) -1-i]
#     if len(mat) % 2 == 1:
#         summ -= mat[len(mat) // 2][len(mat) // 2]

#     return  summ
#     pass


# mat =[[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# # mat = [[1,2,3],
# #               [4,5,6],
# #               [7,8,9]]
# print(diagonal(mat))



def numss(nums):
    numm = float('inf')
    for i in range(len(nums)-1):
        a = int(str(nums[i]) + str(nums[i+1]))
        if a < numm:
            numm = a
    return numm

nums = [23,55,42,21]
print(numss(nums))
