# Fractal-style pyramid:

#         *
#        * *
#       *   *
#      * * * *
#     *       *
#    * *     * *
#   *   *   *   *
#  * * * * * * * *
# *****************


n = 14

for i in range(1, n+1):
    sp  = " "*(n-i+1)
    print(sp, end = "")
    for j in range(2*i-1):
        if i ==n  or i ==n//2+1:
            if j%2 ==0:
                print("*", end ="")
            else:
                print(" ", end ="")
        elif j ==0 or j == 2*i-2 or j ==n or j == 2*i-(n+2): # j ==2 i == 6 j ==4 i ==7
            print("*" , end = "")
        else:
            print(" ", end = "")
    print()

print("*" * (2*n+1))

# n = 8 
# for i in range(1, n+1): 
#     sp = " "*(n-i) 
#     print(sp, end = "") 
#     for j in range(2*i-1): 
#         if j ==0 or j == 2*i-2 or i ==n: 
#                 print("*" , end = "") 
#         else: 
#             print(" ", end = "") 
#     print()