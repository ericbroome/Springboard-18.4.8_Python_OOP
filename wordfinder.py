"""Word Finder: finds random words from a dictionary.

NOTE: There is NO WAY to get doctest to work. I keep getting error "multiple statements found ..."
and there seems to be absolutely NO ANSWER to this problem.
However, manually running what would have been test code, in the terminal, works fine.
I don't have days to spend on this minor project. This doctest issue, with classes, is a major roadblock
and searching the internet literally for hours yields no results. I get the error when instantiating a class
in the doctest. It stops, right there, goes no further. The exact same code works fine in the terminal.

"""

import random

class WordFinder:
    """Find random words in a list
    """
    lst = []

    def __init__(self, path):
        "Read src file into a list"
        self.lst = []
        f = open(path)
        data = f.readlines()
        for line in data:
            self.lst.append(line.rstrip("\n"))
        print(f"{len(self.lst)} lines read")

    def random(self):
        """Returns a random word from the list"""
        rand = random.randint(0, len(self.lst))
        return (self.lst[rand]).rstrip("\n")



class SpecialWordFinder(WordFinder):
    """Find a random word while avoiding comments and blank lines
   """
    def parse(self, path):
        """Readsafile,strips blank lines and comments starting with '#'"""
        self.lst = [line.strip() for line in self.lst if line.strip() and not line.startswith("#")]
        return self.lst