# Triple layer diamond:

#       *
#      ***
#     *****
#    ***#***
#   *****#*****
#  *******@*******
#   *****#*****
#    ***#***
#     *****
#      ***
#       *


n = 6
for i in range(1,n):
    sp = " " *(n-i)
    print(sp , end = "")
    for j in range(2*i-1):
        if i <= (n//2):
            print("*" * (2*i-1), end = "")
        else:
            print("*" *n, end = "")
        print()