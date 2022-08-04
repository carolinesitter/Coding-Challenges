# FIND LUCKY NUMBERS CHALLENGE

# Problem:
## Given an interger, n, return a list containing n unique
## unique random numbers between 1-10, inclusive.
## (this function will never be called with n < 0 or n > 10.)

# Test Case:
## lucky_numbers(3)
## >>> (1,5,9)

# Psuedocode:
## from random import choice(python library)
## write a function that takes in a number
## set a variable called nums to a list of a range of numbers 1-11
## set another variable called lucky_numbers to an empty list
## iterate through the range of the input num 
## for each item in our range of the input num, 
### our input num is equal to a random choice of a number in our list,
### remove num from the numbers list to avoid duplicates
### add num to the lucky_numbers list
## return lucky_numbers list

# Code:
from random import choice

def lucky_numbers(num):
    """ Given a random number, n, return a list of n random numbers."""

    numbers = list(range(1,11))

    lucky_numbers = []

    for i in range(num):
        num = choice(numbers)
        numbers.remove(num)
        lucky_numbers.append(num)
    
    return lucky_numbers


