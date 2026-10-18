def max_summ(nums):
    nums.sort()
    a = []
    b = []
    for i in range(len(nums)):
        f = str(nums[i])
        summ = 0
        for digit in f:
            summ += int(digit)
        a.append(summ)
        # a.sort()
    max_sum = 0
    for i in range(len(a)):

        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                b.append(nums[i]+ nums[j])

    return max(b)

nums = [18,43,36,13,7]

print(max_summ(nums))