# Inverted center pyramid:

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *


n = 5
# for i in range(n,0,-1):
#     print("  " * (n-i) +   "* "* (2*i-1))


# for i in range(n,0,-1):
#     print("  " * (n-i) +   " ".join('*'*(2*i-1)))


for i in range(n,0,-1):
    
    sp = "  " * (n-i)
    line = ''
    for j in range(2*i-1):
        line += "*" + " "
    print(sp + line)