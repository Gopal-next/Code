def three_sum(l):
    l.sort()
    res = []
    for i in range(len(l)):
        if i >0 and l[i] == l[i-1]:
            continue
        left , right = i+1, len(l) -1

        while left< right:
            s = l[i] + l[left] + l[right]
            if s ==0:
                res.append([l[i],l[left], l[right]])

                left += 1
                right -= 1

                while left < right and l[left] == l[left-1]:
                    left += 1
                while left < right and l[right] == l[right -1]:
                    right -= 1
            elif s <0:
                left += 1
            else:
                right -= 1
        
    return res




l = [-1,0,1,2,-1,-4]
print(three_sum(l))