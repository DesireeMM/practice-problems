# you are given the heads of two sorted linked lists list1 and list2
# merge the two lists in a one sorted lists
# the list should be made by splicing together the nodes of the first two lists
# return the head of the merged linked list

# class ListNode:
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next

# pseudocode
# set up base cases where one list is empty
# if both lists, compare the given nodes values
# if the first list value is lower, list1 is the new head
# use recursion to assign next values
# if the second list value is lower, list2 is the new head
# use recursion to assign next values

def merge_two_sorted_lists(list1, list2):
    """Takes in two linked lists node and returns the head of a sorted, merged linked list"""

    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = self.merge_two_sorted_lists(list1.next, list2)
        return list1
    else:
        list2.next = self.merge_two_sorted_lists(list1, list2.next)
        return list2

# solving without recursion

# class ListNode:
    # def __init__(self, val=0, next=None):
        # self.val = val
        # self.next = next

# pseudocode
# need to keep track of the current node
# while both lists exist
# compare values and reassign next as needed
# move to current node's next
# as soon as there is only one list
# reassign next to that list

def merge_two_sorted_lists_no_recursion(list1, list2):
    """Takes in two linked list nodes and returns the head of a sorted, merged linked list"""

    start_node = ListNode(0)
    # we need a starting point to add our sorted nodes
    current_node = start_node

    while list1 and list2:
        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next

        current_node = current_node.next

    if list1:
        current_node.next = list1
    if list2:
        current_node.next = list2

    return start_node.next
