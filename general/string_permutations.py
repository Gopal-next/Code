# Problem: Write a Python function to generate all distinct permutations of a string containing unique characters.

def generate_permutations(s):

    if len(s) == 1:
        return [s]
    perms = []
    for i, char in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for p in generate_permutations(remaining):
            perms.append(char+p)
    return perms


s = "abcde"
ans = generate_permutations(s)
print(ans, len(ans))