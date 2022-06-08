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