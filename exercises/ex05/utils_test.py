"""Tests for only_evens, sub, and concat functions."""


__author__ = "730331514"


from exercises.ex05.utils import only_evens

from exercises.ex05.utils import sub

from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """ Asserts that the function repeats an empty list when given."""
    assert only_evens([]) == []


def test_only_evens_even() -> None:
    """Tests for when one even integer is given."""
    xs: int = 2
    assert only_evens([xs]) == [2]


def test_only_evens_odd() -> None:
    """Tests for when one odd integer is given."""
    xs: int = 3
    assert only_evens([xs]) == []


# SUB TEST


def test_sub_empty() -> None:
    """Tests for when list is empty, and two integers are zero."""
    assert sub([], 0, 0) == []


def test_sub_single_item() -> None:
    """Tests for when provided list is a single item."""
    xs: list[int] = [3]
    assert sub(xs, 0, 0) == [3]


def test_sub_many_items() -> None:
    """Tests for when provided list is multiple items with a negative starting index."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(xs, -1, 4) == [1, 2, 3, 4]


# CONCAT TEST


def test_concat_empty() -> None:
    """Tests for when given lists are empty."""
    assert concat([], []) == []


def test_concat_single_item() -> None:
    """Tests for when each list has one item."""
    xs: list[int] = [3]
    ys: list[int] = [4]
    assert concat(xs, ys) == [3, 4]


def test_concat_many_items() -> None:
    """Tests for when the two given lists contain many items."""
    xs: list[int] = [3, 76, 438]
    ys: list[int] = [37, 1000]
    assert concat(xs, ys) == [3, 76, 438, 37, 1000]