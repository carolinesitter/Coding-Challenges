# IS PALINDROME CHALLENGE

# Problem:
## Return True if a word is a palindrome, False otherwise.
## (A palindrome is a word that is spelled the same backwards and forwards.)

# Test Case:
## is_palindrome("hello")
## >>> False
## is_palindrome("noon")

# Pseudocode:
## define a function that takes in a word as a string
## get the first half of the word via its range
### ( do this by dividing the range by 2)
## iterate through the first half of the range with a for loop
### if the letter at the current (i) index is NOT EQUAL to the letter
### at the last (-i - 1) index,
### return False


## BASIC IDEA: split the word in half and compare the first and last indexes
## to each other and work your way in


# Code:
def is_palindrome(word):
    """ Given a word, return True if it is a palindrome."""

    for letter in range(len(word) // 2):
        if word[letter] != word[-letter - 1]:
            return False
        else:
            return True
