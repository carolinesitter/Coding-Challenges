# CHALLENGE: MOST COMMON WORD

## Given a paragraph and a list of banned words, return the most frequent word
## that is not in the list of banned words. It is a guaranteed that there is at least one word
## that isn't banned and that the answe is unique

# TEST CASE 1
## Input: "Bob hit a ball, the hit ball flew far after it was hit."
## Banned: ["hit"]
## Output: "ball"

# Pseudocode:
## normalize the string (replace non-alphanueric chars to blanks, lowercase)
## tally up every non banned word
## find the word with the max count value and return


# CODE:
## throw banned words into a hash set

class MostCommonWord:
    def most_common_word(self, paragraph: str, banned: list[str]) -> str:
        
        # create an empty dictionary that will tally up the most common words
        word_counter = {}

        # create a hash set of banned words to improve runtime efficency 
        banned_words = set(banned)

        # take the string input and convert it to lowercase,
        # if a word is alphanumeric, replace it with blanks
        normal_str = ''.join(char.lower()
                            if char.isalum() 
                            else ' ' 
                            for char in paragraph)

        # iterate through the modified string and look for non banned
        # words, if its not in our banned words set, add it to a dictionary and begin to
        # tally it up (increase by 1) every time it appears in our list
        for word in normal_str.split():
            if word not in banned_words:
                word_counter[word] = word_counter.get(word, 0) + 1
        

        current_max_count = 0
        max_word = ' '
        
        # iterate over our word counter dictionary and get the value of each
        # word/key. If the value of the word/key is greater than the current max value
        # then set it as the current max value which we will use to get the key/word.
        # Once we have completed iterating through the dictionary, we will have our max 
        # word which we will return (hence setting it to an empty string).
        for word in word_counter:
            if word_counter[word] > curr.max:
                curr_max = word_counter[word]
                max_word = word

        return max_word


# RUNTIME COMPLEXITY:
## Need to study this more -- but it is O(N + B).