"""Exercises for wordle by Yubo Du, my third program in comp110."""

__author__ = "730621860"

secret_word = "python"

# store the length of secret word
length_secret_word: int = len(secret_word)

# I need to check if the input has same numbers of index as secret number.

guess_word: str = input(f"What is your {length_secret_word}-letter guess? ")

# If guess word has different index with secret word, then the system needs to loop until got correct input
while len(guess_word) != len(secret_word):
    re_guess_word: str = input(f"That was not {length_secret_word} letters! Try again: ")
    guess_word = re_guess_word

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

# Assign all variables we will use.
index_number: int = 0
emoji: str = ""

# The outer loop to camprae guess word index and secret word index.
while index_number < (length_secret_word):
    
    re_guess_word_index: str = guess_word[index_number]
    re_secret_word_index: str = secret_word[index_number]
    if re_guess_word_index == re_secret_word_index:
        emoji = emoji + green_box
    if re_guess_word_index != re_secret_word_index:
        
        boolean = False
        alternate_index: int = 0

# The  loop inside used to check if the index of guess word appeared in secret word.       
        while (not boolean) and (alternate_index < len(secret_word)):
            
            if re_guess_word_index == secret_word[alternate_index]:
                boolean = True    
            else:
                alternate_index = alternate_index + 1
                
        if boolean:
            emoji = emoji + yellow_box
        if not boolean:
            emoji = emoji + white_box
    
    index_number = index_number + 1
    
    
# Give the result
print(emoji)

# Give the feedback if their guess word is correct or not.
if guess_word != secret_word:
    print("Not quite. Play again soon!")
if guess_word == secret_word:
    print("Woo! You got it!")