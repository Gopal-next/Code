def countGoodSubstrings(s):
        res = 0
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                res += 1
        return res

s = "xyzzaz"
print(countGoodSubstrings(s))  # Output: 1 (substring "xyz")

s = "aababcabc"
print(countGoodSubstrings(s))  # Output: 4 (substrings "abc", "bca", "cab", "abc")