"""
    check weather the string is anagram of each other  .
"""

def are_anagrams(str1, str2):
    # Sort both strings and compare
    str1 = sorted(str1, reverse=False)
    str2 = sorted(str2, reverse=False)
    return str1 == str2

# Test cases
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
    
    
            