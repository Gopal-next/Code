# Letter triangle:

# A
# AB
# ABC
# ABCD
# ABCDE


n = 5

for i in range(1, n+1):
    a = ''

    for j in range(1, i+1):
        a += chr(j+64)
    print(a)

print(ord('A'))

print(chr(69))