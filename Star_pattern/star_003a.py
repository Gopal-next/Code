#  Center-aligned pyramid:

#       *
#     * * *
#   * * * * *
# * * * * * * * *

# n = int(input("Enter a number : "))
n =4

# for i in range(1, n+1):
#     print("  "*(n-i) + ' '.join('*'*(2*i-1)))

# for i in range(1, n+1):
#     print("  "*(n-i) + "* "*(2*i-1))

# for i in range(1, n+1):
#     for j in range(n-i):
#         print('  ', end = "")
#     for k in range(2*i-1):
#         print("* ", end = "")
#     print()

for i in range(1, n+1):
    sp = "  " * (n-i)
    st = ''
    for j in range(2*i-1):
        st += "*" + ' '
    print(sp+ st)