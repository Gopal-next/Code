# def minDeletions(nums):
#     count  = 0
#     for i in range(len(nums)-1):
#         if nums[i] == nums[i+1]:
#             count += 1
#     return count

# nums = [4,4,9,4]
# print(minDeletions(nums))

def last_visit(grid):
    a = [0,0]
    k = 0
    for i in grid:
        for j in range(len(i)):
            
            if grid[k][j] == 'L' and a[1] <=2:
                a[1] -= 1
            elif grid[k][j] == 'R' and a[1] <= 1:
                a[1] += 1
            elif grid[k][j] == 'U' and a[0] <= 2:
                a[0] -= 1
            elif grid[k][j] == 'D' and a[0] <= 2:
                a[0] += 1
        k += 1 
    return a

grid = [["R","D"],["U","L"]]
# grid= [["R","R","R"]]
# grid= [[1,2],[4,5]]
print(last_visit(grid))

# [1,0]