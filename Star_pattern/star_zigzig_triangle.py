#  Zigzag triangle:

# *
# * *
# *   *
# * * * *
# *       *
# * * * * * *

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

n = 10

# for i in range(1, n+1):

#     for j in range(1, i+1):
#         if i==n or i==j or j==1:
#             print("* ",end="")
#         elif i == (n//2)+1:
#             print("* ", end ="")
#         else:
#             print("  ", end ="")
    
#     print()

rows = 6

for i in range(1, rows + 1):

    # For rows 4 and 6 → full star rows
    if i == 4 or i == 6:
        print("* " * i)

    # For other rows → hollow rows
    else:
        if i == 1:                     # Row 1 → just one star
            print("*")
        else:
            print("*" + " " * (2*i - 3) + "*")
