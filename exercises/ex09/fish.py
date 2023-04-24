"""File to define Fish class."""


class Fish:
    """A class with attribute age."""
    age: int
    
    def __init__(self):
        """An init method called when Fish()."""
        self.age = 0
        return None

    def one_day(self):
        """A method for adding fish's age."""
        self.age = self.age + 1
        return None