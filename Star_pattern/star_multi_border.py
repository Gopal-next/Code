# Multi-border pyramid:

#       *
#      #*#
#     @#*#@
#    $@#*#@$
#   %$@#*#@$%
#  &%$@#*#@$%&

n = ['&','%','$','@','#','*']
# print(n[6])
for i in range(len(n)):
    s = " "*(len(n) -i)
    l = ''
    for j in range(i):
        l += n[(len(n)-1)-j]
    print(s + l + ''.join(reversed(l[:-1])))