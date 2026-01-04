# Wave interference pattern

#         *
#        *~*
#       *~@~*
#      *~@#@~*
#     *~@#$#@~*
#    *~@#$%$#@~*
#   *~@#$%^%$#@~*
#    *~@#$%$#@~*
#     *~@#$#@~*
#      *~@#@~*
#       *~@~*
#        *~*
#         *

s = ['*','~','@','#','$','%','^']

for i in range(1,len(s)+1):
    l = " "*(len(s)-i)
    k = ''
    for j in range(i):
        k += s[j]
    # print(l+"*")

    print(l+k + "".join(reversed(k[:i-1]) )) 

