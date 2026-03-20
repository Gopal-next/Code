def cell_range(nums):
    res = []

    for i in range(ord(nums[0]), ord(nums[3]) + 1):
        for j in range(int(nums[1]), int(nums[4]) + 1):
            res.append(chr(i) + str(j))
    return res


s = "K1:L2"
print(cell_range(s))