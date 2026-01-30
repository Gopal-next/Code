def palindrome(s):
    # filtered_chars = [char.lower() for char in s if char.isalnum()]
    # # Check if the filtered list of characters is the same forwards and backwards
    # return filtered_chars == filtered_chars[::-1]

    return str(s) == str(s)[::-1]

# Example usage:
# print(palindrome("A man, a plan, a canal: Panama"))  # Output: True
# print(palindrome("race a car"))                      # Output: False
print(palindrome(121))                                 
print(palindrome(-121))   
print(palindrome(10))                               