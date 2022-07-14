# CHALLENGE 3: CONCATENATE LISTS

# Given two lists, concatenate them (or combine them)

# Test Case:
## concat_lists([1,4,6], [2,7,3,2])
## >>> [1,4,6,2,7,3,2]

# Pseudocode:
## Define a function that takes in two lists
## add (or concatenate them together)
## Return and print the new list

# Code:
def concat_lists(list1, list2):
    """Take in two lists and concatenate them"""

    new_list = list1 + list2

    return new_list
