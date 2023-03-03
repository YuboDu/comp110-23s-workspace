"""Exercises 5 for more list Utility Functions by Yubo Du, my fifth program in comp110."""


__author__ = "730621860"


def only_evens(input: list[int]) -> list[int]:
    """Used to get the even numbers in input list and make them into a new list and return."""
    new_list: list = []
    for item in input:      # A loop used to check if the item seperately is even, if so, add them in list we return
        if item % 2 == 0:
            new_list.append(item)     # Add even item to our new list and return
    return new_list


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Used to combine input1 and input2, two list as one list."""
    new_list: list[int] = []  # Used to contain all items in list1 and list2. it makes us no need to modify parameter
    for item in input1:    # Make a loop to add items in first list in our new_list
        new_list.append(item) 
    for item in input2:   # Make a loop to add items in second list to our new_list, just followed first list in new list
        new_list.append(item)
    return new_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Used to make a subset of input list based on the range index we input."""
    if start < 0:     # If start is negative, change it to 0
        start: int = 0
    if end > len(input):  # If the end index is greater than the length of the list, change it to the length of input, end with the end of the list.
        end: int = len(input)
    if len(input) == 0:   # If input list is empty, return a empty list
        return []
    if start >= len(input):   # If start index is bigger even than the end of list, return empty list
        return []
    if end == 0:      # If end index is even at the beggining of the list, then return empty list
        return []
    sub_set_of_input: list[int] = []
    for idx in range(start, end):     # A loop used to add all items in list based on the index range we have
        sub_set_of_input.append(input[idx])
    return sub_set_of_input