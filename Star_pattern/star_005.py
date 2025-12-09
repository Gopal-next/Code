# Triangle

#           *
#         *   *
#       *   *   * 
#    *    *   *    * 


n = 4

# for i in range(1,n+1):
#     print("  " *(n-i)   +  "*   "*i)

for i in range(1, n+1):
    sp = "  "*(n-i)
    l = ""
    for i in range(i):
        l += "*"  + "   "
    print(sp + l)