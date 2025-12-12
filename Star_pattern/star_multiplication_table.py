#  Multiplication table triangle:


# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25



n =5

# for i in range(1, n+1):
#     k = 1
#     for j in range(1, i+1):
#         print(i*k, end = " ")
#         k += 1
#     print()


for i in range(1, n+1):
    s = ''
    k = 1
    for j in range(1, i+1):
        s += str(i*k) +" "
        k += 1
    print(s)