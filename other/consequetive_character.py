def consecutive_ch(s):
    """
    Function to check if a string has consecutive characters.
    :param s: Input string
    :return: True if the string has consecutive characters, False otherwise
    """
    c = 1
    d = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            c += 1
        else:
            c = 1
        d = max(d, c)
    return d

s = 'aabbccddeeffggggggddddd'
print(consecutive_ch(s))

s = 'llmmnnooppqqrrssttuuvvwwxxyyzz'
print(consecutive_ch(s))
