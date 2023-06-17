# given two strings, return true if t is an anagram of s
# recall that an anagram is a word or phrase formed by rearranging the
# letters of a different word or phrase, typically using all the original
# letters exactly once
# the input strings will only contain lowercase English letters

# pseudocode
# first check if the strings are the same length
# if not, we can return false
# else create a histogram
# check that histogram values match
# if all match, return True

def is_valid_anagram(s, t):
    """Takes in two strings and returns True if they are valid anagrams"""

    if len(s) != len(t):
        return False
    
    s_dict = {}
    t_dict = {}

    for char in s:
        if char not in s_dict:
            s_dict[char] = 1
        else:
            s_dict[char] = s_dict[char] + 1

    for char in t:
        if char not in t_dict:
            t_dict[char] = 1
        else:
            t_dict[char] = t_dict[char] + 1
    
    for key, val in s_dict.items():
        if key not in t_dict:
            return False
        elif t_dict[key] != val:
            return False
        else:
            continue

    return True

# solution was accepted, beats 79.91% runtime
# problem stated that the input strings would only contain lowercase English letters
# what if the inputs contained Unicode characters?
# because my solution is creating a dictionary with the characters as keys,
# it should still work appropriately