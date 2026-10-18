def word_pattern(pattern, s):

    words = s.split()
    if len(words) != len(pattern):
        return False
    char = {}
    for ch in s:
        if ch not in char:
            pass
            
    pass


pattern = "abba"
s = "dog cat cat dog"

print(word_pattern(pattern, s))