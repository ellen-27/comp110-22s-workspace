"""Test file for dictionary file."""

__author__= "730331514"


from dictionary import invert


from dictionary import favorite_color


from dictionary import count


def test_invert_empty() -> None:
    """ Asserts that function will return an empty dictionary given empty dictionary."""
    assert invert({}) == {}


def test_invert_one_value() -> None:
    """Asserts that, given one set of keys a values, the key and value will swap."""
    xs: dict[str, str] = {'a': 'b'}
    assert invert(xs) == {'b': 'a'}

def test_invert_many_sets() -> None:
    """Asserts that, given many sets of keys and values, each set will be swapped."""
    xs: dict[str, str] = ({'a': 'z', 'b' : 'y', 'c': 'x'})
    assert invert(xs) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_favorite_color_empty() -> None:
    """Asserts that function returns an empty dictionary when given empty dictionary."""
    assert favorite_color({}) == ''

def test_favorite_color_one_set() -> None:
    """Asserts that, when given one set of keys and values, function returns said set."""
    xs: dict[str, str] = {'Jack': 'blue'}
    assert favorite_color(xs) == 'blue'

def test_favorite_color_many_sets() -> None:
    """Asserts that, when given multiple sets, function returns most common value's key."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == 'blue'

def test_count_empty() -> None:
    """Asserts that function returns empty dictionary when given empty list."""
    assert count([]) == {}

# def test_count_one_item() -> None:
#     """Asserts that, when given one index, function returns a dictionary with value of 1."""
#     xs: list[str] = ['okay']
#     assert count[xs] == {'okay': 1}