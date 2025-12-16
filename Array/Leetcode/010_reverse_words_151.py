def reversewords(s):
    st = s.split()
    ll = []
    for i in st:
        ll.append(i)
    return ' '.join(ll[::-1])

    # return ' '.join(s.split()[::-1])


s = "the sky is blue"
# Output: "blue is sky the"
print(reversewords(s))

t = "  hello world  "
# Output: "world hello"
print(reversewords(t))

u = "a good   example"
# Output: "example good a"
print(reversewords(u))