#  Incremental spacing:

# *
# * *
# *  *  *
# *   *   *   *
# *    *    *    *    *


n = 8


for i in range(1, n+1):
    l = ''

    for j in range(1,i+1):
        l += '*' + " " *i
    print(l)
    
    # print("*"*i)