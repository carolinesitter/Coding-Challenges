# CHALLENGE 5: Has More Vowels

# Given a word in English, return True if that word contains more 
# vowels than non-vowels; otherwise, return False. 
# The word will always be a single word, without any punctuation or spaces.
# It will contain only uppercase and lowercase letters.

# Test Case:
## has_more_vowels("hello")
## >>> False
## has_more_vowels("moose")
## >>> True

# Pseudocode:
## define a function that takes in a string
## store list of vowels in a variable
## create two empty lists: one for vowels and one for consonants
## iterate through the string,
### if there is a vowel in the string, add it to the vowels list
### else, add it to the consonants list
## if vowels list > consonants list, return True
## else return False

# Code:
def has_more_vowels(word):
    """ Determine if a word has more vowels than consonants. """

    vowels = "aeiou"

    vowels_list = []
    consonants_list = []

    for letter in word:
        if letter in vowels:
            vowels_list.append(letter)
        else:
            consonants_list.append(letter)
    
    if len(vowels_list) > len(consonants_list):
        return True
        
    else:
        return False