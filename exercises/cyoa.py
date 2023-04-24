"""EX06 - Choose Your Own Adventure. My adventure is coinflip guess in a row game."""

__author__ = "730621860"

from random import randint

points: int = 0

player: str = ""

SMILE_FACE_EMOJI = "\U0001f600"

award_point = 1

lose_point: int = 1


def greet() -> None:
    """A greeting and want player to enter their name!"""
    global player
    print("welcome to this coinflip game, you will guess heads or tails in a row")
    print("If you guess right in a row, you will get point. If worng, you will lose point. Remember, 1 means heads and 2 means tails ")
    print("In five guessses in a row mode, you will get 1 point when you are right and lose 1 point when you are worng")
    print("In ten guessses in a row mode, you will get 10 point when you are right and lose 3 point when you are worng")
    print("Let us see how many points you got!")
    player = input("Choose a player name to begin this adventure!")
    print(f"Welcome {player}, let's begin the adventure!")


def make_five_guesses_in_a_row() -> None:
    """Begin the mode of making 5 guesses in a row!"""
    global points
    
    guess: int = int(input(f"{player}, Enter 5 digits number which represents your 5 guess! {SMILE_FACE_EMOJI}, Remember, 1 means heads and 2 means tails."))
    anwser: int = int(str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)))
    if guess == anwser:
        points = points + award_point
        print(f"Congradulations! {player} You will get one point and it is {points}.")
    if guess != anwser:
        points = points - lose_point
        print(f"Sorry, {player}, you lost one point, it is {points} now.")


def make_10_guesses_in_a_row(input1: int) -> int:
    """Begin the mode of making 10 guesses in a row!"""
    print("Remember, 1 means heads and 2 means tails")
    str_guess: int = int(input(f"{player}, Enter 10 digits number which represents your 10 guess! {SMILE_FACE_EMOJI}, you will get 10 points when right and lost 3 points when wrong."))
    guess: int = int(str_guess)
    anwser: int = int(str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)) + str(randint(1, 2)))
    if guess == anwser:
        input1 = input1 + award_point * 10
        print(f"Congradulations! {player} You will get ten point and it is {input1}.")
    if guess != anwser:
        input1 = input1 - lose_point * 3
        print(f"Sorry, {player}, you lost three point, it is {input1} now.")
    return input1


def main() -> None:
    """The mian function used to continue game or stop the game."""
    greet()
    global points
    branches = 0
    while branches != 3:
        branches: int = int(input("type 1 to begin 5 guess in a row challenge, type 2 to start 10 guess in a row challenge, or type 3 for ending the game"))
        if branches == 1:
            make_five_guesses_in_a_row()
        if branches == 2:
            new_points: int = make_10_guesses_in_a_row(points)
            points = new_points
        
    print(f"Thank you for playing it, {player} {SMILE_FACE_EMOJI} , your final points after this adventure is {points}")
            

if __name__ == "__main__":
    main()