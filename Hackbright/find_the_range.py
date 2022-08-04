# FIND THE RANGE CODING CHALLENGE

# Problem:
## Given a list of numbers, return the largest and smallest number

# Test Case:
## find_range([2,5,8,4,10])
## >>> (2, 10)

# Pseudocode:
## define a function that takes in a list
## set a variable called greatest_num as equal to the first index in the list
## set a variable called smallest_num as equal to the first index in the list
## iterate through each item in the list and compare it to our smallest and equal nums
### if the current item is greater than greatest_num, set num equal to that item,
### if the current item is less than smallest_num, set num equal to that item
### return our smallest and equal nums


# Code:
def find_range(nums):
    """Take in a list of numbers and return the smallest
    and greatest numbers within that list."""

    greatest_num = nums[0]
    smallest_num = nums[0]

    for num in nums:
        if greatest_num < num:
            greatest_num = num

        if smallest_num > num:
            smallest_num = num
        
    return smallest_num, greatest_num