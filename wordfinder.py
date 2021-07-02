"""Word Finder: finds random words from a dictionary.

"""

import random

class WordFinder:
    """Find random words in a list
        >>> wf = WordFinder("words.txt")
        >>> print(len(wf.lst) > 0)
        True
        >>> print(wf.random() in wf.lst)
        True
    """
    lst = []

    def __init__(self, path):
        """Read src file into a list"""
        self.lst = []
        f = open(path)
        data = f.readlines()
        for line in data:
            self.lst.append(line.rstrip("\n"))

    def random(self):
        """Returns a random word from the list"""
        rand = random.randint(0, len(self.lst))
        return (self.lst[rand]).rstrip("\n")



class SpecialWordFinder(WordFinder):
    """Find a random word while avoiding comments and blank lines
        >>> swf = SpecialWordFinder('words.txt')
        >>> print(len(swf.lst) > len(swf.parse('words.txt')))
        True
   """
    def parse(self, path):
        """Readsa file, strips blank lines and comments starting with '#'"""
        self.lst = [line.strip() for line in self.lst if line.strip() and not line.startswith("#")]
        return self.lst