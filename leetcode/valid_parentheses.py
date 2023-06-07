# given a string containing just the characters '(', ')', '[',']', '{', and '}'
# determine if the input string is valid
# an input string is valid if:
# - open brackets must be closed by the same type of bracket
# - open brackets must be closed in the correct order
# - every close bracket has a corresponding open bracket of the same type

# example input
# s = "()"
# output = true

# pseudocode:
# function will take in a string as an argument
# function should return a boolean
# true if meets above conditions

# iterate through each character in the string
# if the character matches one of the open bracket types
# add that character to the stack
# the next close bracket type must be of the matching type
# if matching type, pop open from stack
# return true

def valid_parentheses(str):

    bracket_stack = []
    bracket_dict = {")": "(", "}": "{", "]": "["}

    for char in str:
        if char in "({[":
            bracket_stack.append(char)
        elif char in ")}]":
            if bracket_stack and bracket_stack.pop() == bracket_dict[char]:
                continue
            else:
                return False

    if bracket_stack:
        return False

    return True