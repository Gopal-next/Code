def increasing_decreasing_str(strr):
    freq= {}

    for i in strr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    res = []
    while len(res) < len(s):
        for ch in sorted(freq.keys()):
            if freq[ch] > 0:
                res.append(ch)
                freq[ch] -=1
        for ch in sorted(freq.keys() , reverse=True):
            if freq[ch] > 0:
                res.append(ch)
                freq[ch] -= 1
    return ''.join(res)
    # pass


s = "aaaabbbbcccc"
print(increasing_decreasing_str(s))

t = "rat"
print(increasing_decreasing_str(t))


a = {'d': 4, 'b': 4, 'c': 4}
for i  in sorted(a):
    print(i)

print(ord('a'))

