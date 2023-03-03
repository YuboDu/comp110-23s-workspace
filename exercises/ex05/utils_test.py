"""Exercises 5 for Unit test by Yubo Du, my fifth program in comp110."""


__author__ = "730621860"


from exercises.ex05.utils import only_evens, sub, concat


"""Below is the test for function only_evens."""


def test_empty() -> None:     
    """Used to test can this function only_evens run with a empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_many_positive_int() -> None:    
    """Used to test can this function only_evens to find all evens when list consist of positive numbers."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(test_list) == [2, 4, 6]


def test_negative_int() -> None:      
    """Used to test can this function only_evens to find all evens when list consist of positive and negative numbers."""
    test_list: list[int] = [1, -2, -3, 4, -5, 6, 7]
    assert only_evens(test_list) == [-2, 4, 6]


"""Below is the test for function concat."""


def test_concat_empty_list() -> None:   
    """Used to test can function concat, concat two empty list."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_concat_list_with_multiple_elements() -> None:     
    """Used to test can function concat, concat two multiple elements list."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [1, 3, 10, 11]
    assert concat(test_list1, test_list2) == [1, 2, 3, 1, 3, 10, 11]


def test_concat_list_with_single_elements() -> None:    
    """Used to test can function concat, concat two single element list."""
    test_list1: list[int] = [1]
    test_list2: list[int] = [-100]
    assert concat(test_list1, test_list2) == [1, -100]


"""Below is the test for function sub."""


def test_sub_when_start_end_are_correct() -> None:  
    """Used to test sub fuction get right subset when start and end are inputed in right way."""
    test_list: list[int] = [11, 22, 3, 4]
    test_start: int = 0
    test_end: int = 2
    assert sub(test_list, test_start, test_end) == [11, 22]


def test_sub_when_start_bigger_than_length_of_list() -> None:      
    """Used to test sub fuction get right subset when start point is even over the last index of list."""
    test_list: list[int] = [11, 22, 3, 4]
    test_start: int = 100000000
    test_end: int = 2
    assert sub(test_list, test_start, test_end) == []


def test_sub_when_end_bigger_than_length_of_list() -> None:      
    """Used to test sub fuction get right subset when end index we inputed is over the end of list."""
    test_list: list[int] = [11, 22, 3, 4]
    test_start: int = 0
    test_end: int = 10000000
    assert sub(test_list, test_start, test_end) == [11, 22, 3, 4]