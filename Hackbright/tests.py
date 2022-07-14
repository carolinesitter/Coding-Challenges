import pangram, concatenate_lists
import unittest

from pangram import is_pangram
from concatenate_lists import concat_lists

class Pangram(unittest.TestCase):
    """Test if a string is a pangram or not."""

    # Write a test to check if our pangram function works
    def test_is_pangram(self):

        # If we write, "I love cats!" we should get a False return value
        assert(is_pangram("I love cats!") == False)

        # If we insert an actual pangram, we should get a True return value
        assert(is_pangram("Amazingly few discotheques provide jukeboxes.") == True)

class ConcatenateLists(unittest.TestCase):
    """Test if a list of strings is concatenated together."""

    # Write a test to check if our concat_lists function works
    assert(concat_lists([1,4,6],[2,3]) == [1,4,6,2,3])

if __name__ == '__main__':
    unittest.main()