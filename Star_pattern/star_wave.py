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

# s = ['*','~','@','#','$','%','^']
# s = ['◊','△','○','●','◉','★','◇','◆','▣']

s = ['∴','·','○','●','◉','※','★','◆','▲','●','■']

for i in range(1,len(s)+1):
    l = " "*(len(s)-i) 
    k = ''
    for j in range(i):
        k += s[j]
    # print(l+"*")

    print(l+k + "".join(reversed(k[:i-1]))) 


for j in range(len(s),1,-1):
    p = " " *(len(s) - j+1)
    r =''
    for i in range(j-1):
        r += s[i]
    print(p+r+ "".join(reversed(k[:i])))
