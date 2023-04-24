"""File to define Bear class."""


class Bear:
    """A class defined Bear eat, age, hunger socres."""
    age: int
    unger_score: int
        
    def __init__(self):
        """An init method call when we get Bear()."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """A method of changing the age and hunger score of bears."""
        self.age = self.age + 1
        self.hunger_score = self.hunger_score - 1
        return None
    
    def eat(self, num_fish: int):
        """Used to add bears' hunger score based on fish they eat."""
        self.hunger_score = self.hunger_score + num_fish