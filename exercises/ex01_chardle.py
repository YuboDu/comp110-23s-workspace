"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730621860"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

single: str = input("Enter a single character: ")
if len(single) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for", single, "in", word)

frequncy: int = 0

if single == word[0]:
    print(single, "found at index 0")
    frequncy = frequncy + 1
if single == word[1]:
    print(single, "found at index 1")
    frequncy = frequncy + 1
if single == word[2]:
    print(single, "found at index 2")
    frequncy = frequncy + 1
if single == word[3]:
    print(single, "found at index 3")
    frequncy = frequncy + 1
if single == word[4]:
    print(single, "found at index 4")
    frequncy = frequncy + 1

if frequncy == 1:
    print("1 instance of", single, "found in", word)
if frequncy == 0:
    print("No instances of", single, "found in", word)
if frequncy > 1:
    print(frequncy, "instances of", single, "found in", word)