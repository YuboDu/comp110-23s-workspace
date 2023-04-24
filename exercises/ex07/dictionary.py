"""EX07 - Dictionary Functions by Yubo Du my function skeletons and implementations below."""

__author__ = "730621860"


def invert(input1: dict[str, str]) -> dict[str, str]:
    """A function used to swtich the keys and values of the dict we input."""
    output_dict: dict[str, str] = dict()
    for keys in input1:
        output_dict[input1[keys]] = keys
    if len(output_dict) != len(input1):
        raise KeyError
    return output_dict


def favorite_color(input1: dict[str, str]) -> str:
    """A function used to check what is the color that shows mostly in dictionary value."""
    list_of_values: list[str] = []
    
    empty_dict: dict[str, int] = dict()
   
    for keys in input1:
        list_of_values.append(input1[keys])
    
    for elements in list_of_values:
        if elements in empty_dict:
            empty_dict[elements] += 1
        if elements not in empty_dict:
            empty_dict[elements] = 1
    most_frequncy_color: str = list_of_values[0]
    for keys in empty_dict:
        for key in empty_dict:
            if empty_dict[keys] > empty_dict[key]:
                most_frequncy_color = keys
    return most_frequncy_color


def count(input1: list[str]) -> dict[str, int]:
    """A function used to check how many time a element shows in list and make it into a dictionary."""
    empty_dict: dict[str, int] = dict()
    for elements in input1:
        if elements in empty_dict:
            empty_dict[elements] += 1
        if elements not in empty_dict:
            empty_dict[elements] = 1
    return empty_dict