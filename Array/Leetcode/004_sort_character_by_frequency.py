def frequnecysort(s):
    freq = {}
    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] =1
        else:
            freq[s[i]] += 1
    sorrt = sorted(freq.items(), key = lambda x : x[1], reverse=True)
    r = ''
    a = []
    for i , count in sorrt:
        r += i * count
    return r


s = 'tree'
print(frequnecysort(s))