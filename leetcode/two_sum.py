# given an array of integers nums and an integer target,
# return the indices of the two numbers such that they add up to target
# you may assume that each input would have exactly one solution
# you may not use the same element twice
# you can return the answer in any order

# pseudocode
# will need a list to hold answer
# will need to loop through the array

# example input
# nums = [2, 7, 11, 15]
# target = 9

def two_sum(nums, target):
    results = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                results.extend([i, j])
                return results
# runtime is O(n^2) for nested loop

# can you come up with an algorithm that is less than O(n^2) time complexity?

# pseudocode
# recall that indexing, appending, and popping are O(n)
# recall that using different data structures can reduce runtime

def two_sum_faster(nums, target):
    """two_sum function made O(n) by eliminating nested loop"""
    for i, num in enumerate(nums):
        to_find = target - num
        index1 = i
        if to_find in nums and nums.index(to_find) != index1:
            index2 = nums.index(to_find)
            return [index1, index2]

    return []

def two_sum_with_dict(nums, target):
    """two_sum function made O(n) by using dictionary"""
    num_dict = {}

    for i in range(len(nums)):
        to_find = target - nums[i]
        if to_find in num_dict:
            return [num_dict[to_find], i]
        num_dict[nums[i]] = i

    return []
