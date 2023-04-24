"""Exercises 4 for list Utility Functions by Yubo Du, my third program in comp110."""

__author__ = "730621860"


def all(input: list[int], input2: int) -> bool:
    """This is a duction used to check if the int exsist in the list we have."""
    if len(input) == 0:
        return False         # If list is empty, it will return False
    list_index: int = 0
    number_of_index_matches: int = 0      # used to count the how many elements in list same as the argument int
    
    while list_index < len(input):
        if input2 == input[list_index]:
            number_of_index_matches += 1      # If int exist once in list, add 1
        list_index += 1
    
    if number_of_index_matches == len(input):     # Return True if all numbers in list match the indicated number int
        return True
    else:
        return False        # Return False if not all numbers in list match the indicated number int
    

def max(input: list[int]) -> int:
    """This is a function used to return the biggest int in the list."""
    if len(input) == 0:        # If input is empty list, then raise error
        raise ValueError("max() arg is an empty List")
    biggest_int_in_list: int = input[0]    # Set initial biggest int
    index: int = 0
    
    while index < len(input):
        
        if input[index] > biggest_int_in_list:   # Change biggest int if we countered a bigger one
            biggest: int = input[index]
            biggest_int_in_list: int = biggest
        index += 1
    return biggest_int_in_list   # After the loop, after we campared all int in list, we save the biggest int and Return it


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """This function used to check if two input list are identical."""
    if len(input1) != len(input2):     # If their length is not same, they are not equal, then return False
        return False
    index: int = 0     # Set a index to check if their element in index are same one by one
    number_of_correctness: int = 0      # To count how many elements in same index are correct
    
    while index < len(input1):
        if input1[index] == input2[index]:    # To test if the elements in them are same one by one
            number_of_correctness += 1    # If once get a same, then we add one
        index += 1
    
    if number_of_correctness == len(input1):    # If all pairs in these two elements are right, return Ture
        return True
    else:                     # return an error even if one is different
        return False 