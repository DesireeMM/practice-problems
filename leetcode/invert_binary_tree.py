# given the root of a binary tree, invert the tree, and return its root
# class TreeNode:
#   def __init__(self), val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

# based on the examples, we will be swapping the left and right child nodes

# pseudocode
# take in a root node of a tree
# for each node, if there is a left and right node, swap
# return root node

def invert_binary_tree(root):
    """Takes in a root TreeNode for a binary tree, inverts the tree, and returns the new root"""

    if not root:
        return

    nodes_to_check = [root]

    while nodes_to_check:
        current = nodes_to_check.pop()
        if current.left and current.right:
            left_node = current.left
            right_node = current.right
            current.left = right_node
            current.right = left_node
            nodes_to_check.extend([left_node, right_node])
        elif current.left and not current.right:
            current.right = current.left
            current.left = None
            nodes_to_check.append(current.right)
        elif current.right and not current.left:
            current.left = current.right
            current.right = None
            nodes_to_check.append(current.left)

    return root

# the above solution was accepted, but only beats 17.72% for runtime
# try to code using recursion

# pseudocode
# will need a base case
# if not root
# call function on left and right nodes
# function should swap nodes

def invert_tree_recursively(root):
    """Takes in a root node and inverts binary tree recursively. Returns new root"""

    if not root:
        return
    
    invert_tree_recursively(root.left)
    invert_tree_recursively(root.right)

    left_node = root.left
    right_node = root.right
    root.left = right_node
    root.right = left_node

    return root

# beats 72.65% for runtime