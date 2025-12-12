# Hollow center pyramid:

#     *
#    * *
#   *   *
#  *     *
# *********

n = 5
# for i in range(1,n+1):
#     sp  = " "*(n-i)
#     print(sp, end = "")
#     for j in range(2*i-1):
#         if i ==n or j==0 or j ==2*i-2:
#             print("*", end = "")
#         else:
#             print(" ", end ="")

#     print()
    # print(" " *(n-i)   +"*"*(2*i-1))


for i in range( 1, n+1):
    print(" "*(n-i), end = "")
    if i ==1:
        print("*")
    elif i ==n:
        print("*"*(2*n-1))
    else:
        print("*" + " " *(2*i-3) + "*")