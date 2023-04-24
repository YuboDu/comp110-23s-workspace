"""File to define River class."""

__author__ = "730621860"


from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """A class River with attributes day, bears, and fish."""
    day: int
    bears: list
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears.
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """A method for checking the fish of bears and fish then remove or keep them by it."""
        new_fish_list: list[Fish] = []
        new_bears_list: list[Bear] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish_list.append(x)
        for x in self.bears:
            if x.age <= 5:
                new_bears_list.append(x)
        self.fish: list[Fish] = new_fish_list
        self.bears: list[Bear] = new_bears_list
        return None

    def bears_eating(self):
        """Method for how many fishes been eaten what's the outcome to bears huger and fish number."""
        for each_bears in self.bears:
            if len(self.fish) >= 5:
                each_bears.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Check if the bears are so hunger that they will die."""
        new_bears_list: list[Bear] = []
        for all_bears in self.bears:
            if all_bears.hunger_score >= 0:
                new_bears_list.append(all_bears)
        self.bears: list[Bear] = new_bears_list

        return None
        
    def repopulate_fish(self):
        """Check how the bear reproduce and the outcome of it to their population."""
        num_to_add: int = (len(self.fish) // 2) * 4
        while num_to_add > 0:
            self.fish.append(Fish())
            num_to_add = num_to_add - 1
        return None
    
    def repopulate_bears(self):
        """Check how the bear reproduce and the outcome of it to their population."""
        num_to_add: int = len(self.bears) // 2
        while num_to_add > 0:
            self.bears.append(Bear())
            num_to_add = num_to_add - 1
        return None
    
    def view_river(self):
        """Check the river situation."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """A river cycle for several days."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove the rish."""
        frontmost: int = 0
        while frontmost < amount:
            self.fish.pop(frontmost)
            frontmost = frontmost + 1