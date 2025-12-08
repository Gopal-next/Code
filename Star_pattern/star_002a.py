# Left-aligned triangle

# * * * * *
# * * * *
# * * *
# * *
# *
n = int(input("Enter a number : "))
# for i in range(n):
#     print("* "*(n-i))

for i in range(n,0,-1):
    s = ''
    for j in range(i):
        s += '*' + ' '
    print(s)

for i in range(n):
    print(' '.join('*'*(n-i)))