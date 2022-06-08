import hackbright_challenges
import unittest

from hackbright_challenges import is_pangram

class Pangram(unittest.TestCase):
    """Test if a string is a pangram or not."""

    # Write a test to check if our pangram function works
    def test_is_pangram(self):

        # If we write, "I love cats!" we should get a False return value
        assert(is_pangram("I love cats!") == False)

        # If we insert an actual pangram, we should get a True return value
        assert(is_pangram("Amazingly few discotheques provide jukeboxes.") == True)

if __name__ == '__main__':
    unittest.main()