import math
def construct_rectangle(area):
    # len = area
    # br = 1

    # for w in range(1, area+1):
    #     if area %w == 0:
    #         L  = area //w
    #         if L >= w and len - br > L -area:
    #             len, br = L, w
    # return [len, br]

    w = 1
    for i in range(1, area+1):
        if i*i > area:
            w = i -1
            break
    while area % w !=0:
        w -=1 
    L = area//w
    return [L,w]
            
    # return len
    # w = int(math.isqrt(a))
    # while a %w !=0:
    #     w -=1
    # return [a//w,w]



area = 4
print(construct_rectangle(area))

ar = 37
print(construct_rectangle(ar))

are = 122122
print(construct_rectangle(are))
