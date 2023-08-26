import random

"""
Works cited:
GeeksforGeeks. (2022). How to remove blank lines from a .txt file in Python. GeeksforGeeks. https://www.geeksforgeeks.org/how-to-remove-blank-lines-from-a-txt-file-in-python/
"""
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    """__init__:
        - wordpath is used to locate txt file on users disc "/Users/student/words.txt"

        - lines = [line.wstrip() for line in f]:
        removes any white spaces on each line and keeps string. each string has it's on index in list

        - (not sure what self.lines does. Is that necessary?)

        - returns length of lines list
    """
    def __init__(self, wordpath):
        self.wordpath = wordpath
        with open(wordpath) as f:
            lines = [line.strip() for line in f]
        self.lines = lines
        print(f"{len(lines)} words read")
    
    """
    WordFinder.random()
    - Returns a random word from self.lines

    - Unforunately returns empty lines in between lines that contain content

    - Also returns comments '#'

    - I'd like to prevent that from happening... Any suggestions?

    """
    def random(self):
        return random.choice(self.lines)
    

class solutionWordFinder:
    def __init__(self,path):

        selected_file = open(path)

        """Quesiton? How does this work? I always struggled with understanding how to call functions in order to assist __init__"""
        self.words = self.parse(selected_file)

        print(f"{len(self.words)} words read")
    
    def parse(self, selected_file):
        """Parse selected_file -> list of words."""

        return [w.strip() for w in selected_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

class solutionSpecialWordFinder(solutionWordFinder):
    """Question:
        How does this account for empty lines in between lines that contain strings? I tested it on my broken class. Empty lines in between lines that contains strings return ''.
        I think I answered my own question. Strip removes all blank lines already. I was using r.strip() in during my original attempt. Still want to be able to understand "and not" logic.
    """
    def parse(self, selected_file):
        return [w.strip() for w in selected_file if w.strip() and not w.startswith('#')]

    
    
            

        

       



