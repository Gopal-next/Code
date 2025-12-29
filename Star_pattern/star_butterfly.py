# Butterfly with body:

# *       *
# **     **
# ***   ***
# **** ****
# *********
# **** ****
# ***   ***
# **     **
# *       *

n = 5
for i in range(1,n):
    print("*" *i  + " " *(2*(n-i) -1) + "*" *i)
print("*"*(2*n-1))
for i in range(n-1,0,-1):
    print("*" * i + " " * (2 * (n - i) - 1) + "*" * i)