#  Staircase descending:

#     ****
#     ***
#   ***
#   **
# **
# *

n = 6
k = 7
for i in range(n,1,-1):
    print( " " * k  +        "*" *i)
    print( " " * k +  "*" *(i-1))
    k -= 2




