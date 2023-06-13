# a phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters
# it reads the same forward and backward
# given a string, s, return true if it is a palindrome and false otherwise

# pseudocode
# strip string of non-alphanumeric characters
# possibly by appending to a list
# then joining the list
# check if the reverse is equivalent
# return true if passes check

def is_palindrome(s):
    """Takes in a string and returns Boolean true if the string is a palindrome"""

    s_list = []

    for char in s:
        if char.isalnum():
            s_list.append(char.lower())

    reversed_list = reversed(s_list)

    new_s = "".join(s_list)
    reversed_s = "".join(reversed_list)

    if new_s == reversed_s:
        return True
    else:
        return False