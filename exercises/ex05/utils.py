"""This docstring will be edited later."""

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
    """Returns items of given indeces within a list."""
    i = start_index
    subset: list[int] = list()
    while i < len(x):
        if i < 0:
            i = 0
        if end_index > len(x):
            end_index = len(x)
        while end_index > i:
            subset.append(x[i])
            i += 1
        i += 1    
    return subset

def concat(x: list[int], y: list[int]) -> list[int]:
    """Returns list that encompasses each given list."""
    i: int = 0
    new_list: list[int] = list(x)
    while i < len(x):
        new_list.append(x[i])
        i += 1
    if i == len(x):
        i = 0
        while i < len(y):
            new_list.append(y[i])
            i += 1
    return new_list
