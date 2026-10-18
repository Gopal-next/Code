def unique(s):
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    seen = set()
    print(freq)
    for i, key in freq.items():
        if key in seen:
            return False
        seen.add(key)
    return True
arr = [1,2,2,2,1,1,3]
print(unique(arr))