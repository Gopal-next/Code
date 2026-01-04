# Spiral tower with borders:

#     |||||
#     |***|
#     |*1*|
#     |***|
#    ||***||
#    |*2*2*|
#    ||***||
#   |||***|||
#   |*3*3*3*|
#   |||***|||
#  ||||***||||
#  |*4*4*4*4*|
#  ||||***||||

n = 4
print(" " * (n-1) + "|"*5)
# for i in range(1,n+1):
#     sp = " "*(n-i)
#     l = ''
#     c = 1
#     for j in range(1,3+2*i+1):
#         if j <= i or j >= 4+i:
#             l += '|'
#         else:
#             l += '*'
#     k = sp+l
#     print(k *3, end ="\n")

for j in range(1, n+1):
    s = " " *(n-j)
    bar = "|"*j 
    star = "*"*3
    num = ('*' + str(j))*j + '*'
    print(s +bar+star +bar)
    print(s+"|"+num +"|")
    print(s+bar+star +bar)
    