#  Hollow triangle:

# *
# **
# * *
# *  *
# *****


n = 6

for i in range(1,n+1):
    for j in range(1,i+1):
        if i ==1 or i ==n or j ==1 or j ==i:
            print("*", end ="")
        else:
            print(" ", end ="")
    print()

# for i in range(1, n+1):
#     star = ''
#     if i ==1:
#         star += "*"
#     elif i ==n:
#         star += "*" *n
#     else:
#         star +="*" + " "*(i-2) + "*"
#     print(star)