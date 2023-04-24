"""EX07 - Dictionary Functions by Yubo Du Test file."""

__author__ = "730621860"


from exercises.ex07.dictionary import invert
import pytest
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
# The test below is used to test fuction invert.


def test_normal_dict() -> None:
    """Used to test the normal dictionary we input."""
    assert invert({'a': 'm', 'b': 'g', 'c': 'x'}) == {'m': 'a', 'g': 'b', 'x': 'c'}


def test_KeyError() -> None:
    """Used to test if it will output keyerror if the keys in output_dict may repeat."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'alex', 'michael': 'alex'}
        invert(my_dictionary)


def test_empty_dict() -> None:
    """Used to test what will return if the input is empty dict."""
    assert invert({}) == {}


# The test below is used to test fuction favorite_colo.


def test_normal_dict_check_2_color() -> None:
    """Used to check when we input the normal dictionary."""
    assert favorite_color({"Marc": "red", "Ezri": "red", "Kris": "blue"}) == "red"


def test_when_exists_several_favorite_color() -> None:
    """Used tp test if some colors shows same times."""
    assert favorite_color({"Marc": "green", "Ezri": "red"}) == "green"


def test_normal_dict_check_4_color() -> None:
    """Used to test when 4 people gave the color they like."""
    assert favorite_color({"Marc": "green", "Ezri": "red", "Bob": "green", "Alex": "yellow", "Alyx": "blue"}) == "green"


# The test below is used to test fuction count.


def test_normal_list_elements_shows_1_time() -> None:
    """Used to test when we only input list with variables show single time."""
    assert count(["pig", "cat", "cow"]) == {'pig': 1, 'cat': 1, 'cow': 1}


def test_normal_list_elements_shows_several_time() -> None:
    """Used to test when we input a list with variables show many times."""
    assert count(["pig", "cat", "cow", "pig", "cat", "pig", "pig"]) == {'pig': 4, 'cat': 2, 'cow': 1}


def test_empty_list() -> None:
    """Used to test when we input empty list."""
    assert count([]) == {}