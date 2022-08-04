# UNIQUE CHARACTERS

# Problem:
## Given a word, return True if it contains only unique characters,
## return False otherwise.

# Test Case:
## unique_chars("hello")
## >>> False
## unique_chars("smile")
## >>> True

# Psuedocode:
## define a function that takes in a word as a string
## define a variable "char_check" is an set of the word
## if the length of the word is equal to the length of the set,
## return True

# Code:
def unique_chars(word):
    """ Given a word, return True if it contains only unique characters."""

    char_check = set(word)

    if len(char_check) == len(word):
        return True
    else: 
        return False
