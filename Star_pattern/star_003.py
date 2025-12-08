# Center-aligned pyramid:

#     *
#    ***
#   *****
#  *******
# *********

# n = int(input("Enter a number : "))
# for i in range(1,n+1):
#     print(' '*(n-i) + "*" * (2*i-1))


# for i in range(1, n+1):
#     space = " " * (n-i)
#     star = "*" * (2*i-1)
#     print(space+star)

# for i in range(1, n+1):
#     line = ""
#     for j in range(i):
#         line += " "*(n-i)
#     for k in range(i):
#         line += "*" *(2*k-1)
    
#     print(line)

n =4


def pyramid(i, n):
    if i > n:
        return
    print(" "*(n-i) + "*"*(2*i-1))
    pyramid(i+1, n)

pyramid(1, n)