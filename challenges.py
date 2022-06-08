# CHALLENGE 1: PRINT DIGITS BACKWARDS

## Given an interger, print each digit in reverse order
## DO NOT solve this by turning the number into a string
## and reversing, use math.

# Test Case:
## >>> print_digits(314)
## 4
## 1
## 3

# Pseudocode:
## define a function that takes in an interger
## set up a while loop
## Set the next digit to equal the number divided by 10
## print each digit
## subtract the last digit from the num total and divide by 10
## to get the next digit 

# Code:
def print_digits(num):
    """Given an interger, print the digits in reverse order, starting with the
        ones place"""

    while num:
        next_digit = num % 10
        print(next_digit)
        num = (num-next_digit) // 10