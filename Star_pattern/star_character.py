# Character pyramid:

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA



n = 5

for i in range(1, n+1):

    sp = " "*(n-i)
    a = ''

    for j in range(1, i+1):
        a += chr(j+64)
    print(sp +a + a[-2::-1])

k = 'AB'
print(k[-2::-1])

print(ord('A'))

print(chr(69))