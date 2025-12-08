# Right-aligned triangle

# *
# * *
# * * *
# * * * *
# * * * * *

n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print("* "*i)

# other way

for i in range(1, n+1):
    star = ''
    for j in range(i):
        star += '*' + " "
    print( star)

# other 

for i in range(1, n+1):
    print(' '.join('*'*i))