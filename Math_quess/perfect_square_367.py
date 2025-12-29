import math
def perfect_square(num):
    if num < 0:
        return False
    i = 1
    while i*i <=num:
        if  i*i == num:
            return True
        i += 1
    return False
            
            
    # n =  int(math.sqrt(num))
    # if n * n == num:
    #     return True
    # return False

n = 16
print(perfect_square(n))

nn = 14
print(perfect_square(nn))