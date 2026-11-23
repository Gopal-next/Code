def max_water(height):
    max_area = 0
    li = []
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            width = j-i

            area = min(height[i], height[j]) * width 
            li.append(area)
            max_area = max(max_area, area)
    return max_area, li


height = [1,8,6,2,5,4,8,3,7]
print(max_water(height))

eightt = [1,1]
print(max_water(eightt))