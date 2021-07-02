"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    start = 0
    next = 0
    def __init__(self, start):
        "Initialize the SerialGenerator with a starting number"
        self.start = start
        self.next = self.start
    
    def __repr__(self):
        "Return information about the current statusof the SerialGenerator instance"
        return f"<SerialGenerator start={self.start} next={self.next}"

    def generate(self):
        "Generate the next number while"
        self.next += 1
        return self.next - 1

    def reset(self):
        "Rest the SerialGenerator to start values"
        self.next = self.start
