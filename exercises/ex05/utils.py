"""A collection of different functions."""


__author__ = "730331514"


def only_evens(xs: list[int]) -> list[int]:
    """Returns even numbers in a list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0: 
            evens.append(xs[i])
            i += 1
        else:
            i += 1
    return evens


def sub(x: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns items of given indeces range within a list."""
    i = start_index
    if start_index < end_index:
        end_index -= 1
    subset: list[int] = list()
    if start_index < 0:
        i = 0
    if end_index > len(x) - 1:
        end_index = len(x) - 1
    while i < len(x):
        while end_index >= i:
            subset.append(x[i])
            i += 1
        i += 1    
    return subset


def concat(x: list[int], y: list[int]) -> list[int]:
    """Returns list that concatenates both given lists."""
    i_x: int = 0
    i_y: int = 0
    new_list: list[int] = list()
    while i_x < len(x):
        new_list.append(x[i_x])
        i_x += 1
    while i_y < len(y):
        new_list.append(y[i_y])
        i_y += 1
    return new_list