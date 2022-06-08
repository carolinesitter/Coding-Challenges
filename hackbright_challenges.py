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


# CHALLENGE 2: PANGRAM

# A pangram is a sentence that contains all the letters of the English alphabet
# at least once, like "The quick brown fox jumps over the lazy dog." Write a 
# function to check if a sentence is a pangram or not.

# Test Case: 
## >>> is_pangram("The quick brown fox jumps over the lazy dog")
## True
## >>> is_pangram("I love cats")
## False

# Pseudocode:
## define a function that takes in a string
## create an empty set
## loop over each item in the string and check if it is alpha
## if so, add it to our set
## if length of set is equal to 26, return true ... else return false

# Code:
def is_pangram(string):
    """Check if the string is a pangram, if so return true"""

    letters = set()

    for item in string:
        if item.isalpha():
            letters.add(item)

    if len(letters) >= 26:
        return True
    
    else:
        return False
