"""Exercises 3 for Structured Wordle by Yubo Du, my third program in comp110."""

__author__ = "730621860"


def contains_char(str1_being_searched_through: str, str2_being_searched_for: str) -> bool:
    """This is a function used to check if str2(one single character) exsits in str 1(a string)"""
    assert len(str2_being_searched_for) == 1  #shut down the program when str2 is not one charachter.
    
    str1_index: int = 0
    while str1_index < len(str1_being_searched_through):
        bool_value: bool = False
        if str1_being_searched_through[str1_index] == str2_being_searched_for:
            return not bool_value
        str1_index = str1_index + 1
    return bool_value



def emojified(guess_word: str, secret_word: str) -> str:
    """This is a fuction used to check if character in guess word exist in secret word and give a
     set of color box to show it."""
    assert len(guess_word) == len(secret_word)  #shut down the program when the length of guess and secret word is different.
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    guess_word_index = 0
    emoji: str = ""
    
    while guess_word_index < len(guess_word):           # If the character in the same index as secret word, add green
        if guess_word[guess_word_index] == secret_word[guess_word_index]:
            emoji = emoji + green_box
        
        if guess_word[guess_word_index] != secret_word[guess_word_index]: # If not in same index, to check if 
            boolean = contains_char(secret_word, guess_word[guess_word_index])   # if it is not in certian index, then try next one
            
            if boolean:
                emoji = emoji + yellow_box
            if not boolean:                          # If it exist, add yellow box. if not, add white box
                emoji = emoji + white_box
        guess_word_index = guess_word_index + 1
    return emoji                                     #return the emoji box

def input_guess(length_guess_word: int) -> str:      
    """This fuction used to check if the length of guess word is right as the word secret word."""
    guess_word: str = input(f"Enter a {length_guess_word} character word: ") 
    while length_guess_word != len(guess_word):   # If the length of guess word is different, then try gian repeatedly
        guess_word_again: str = input(f"That wasn't {length_guess_word} chars! Try again: ")
        guess_word = guess_word_again
    return guess_word


def main() -> None:
    """This function is used to creat a 6 round game and combine the return of previous function 
    to show if the guesser is right"""
    secret_word = "codes"         #define secret word.
    turn_number: int = 1
    while turn_number <= 7:          
        if turn_number < 7:   # a loop for turn 1-6.
            print(f"=== Turn {turn_number}/6 ===")  
            guess_word = input_guess(len(secret_word))   # call the fuction that make sure guess word has same number of characters as secret word
            print(emojified(guess_word, secret_word))    #call the fuction to get color box above
            if guess_word == secret_word:
                print(f"You won in {turn_number}/6 turns!")
                return None
        turn_number = turn_number + 1
        if turn_number == 7:     # if the turn become 7, then we will stop the loop and end the guess.
            print("X/6 - Sorry, try again tomorrow!")
            print("")
            return None

if __name__ == "__main__":
    main()