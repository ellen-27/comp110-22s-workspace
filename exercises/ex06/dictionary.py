"""Dictionary exercise."""

__author__ = "730331514"

def invert(x: dict[str, str]) -> dict[str,str]:
    """Inverts the keys and values in parameter."""
    y: dict[str, str] = {}
    for key in x:
        y[x[key]] = key
        # if key == y[x[key]]:
        #     raise KeyError
    return y

def favorite_color(x: dict[str, str]) -> str:
    """Returns most common favorite color ('person':'color')."""
    favorite: str = ""
    count_freq: dict[str, int] = {}
    for color in x:
        if x[color] in count_freq:
            count_freq[x[color]] += 1
        else:
            count_freq[x[color]] = 1
        # if count_freq[x[color]] == count_freq[x[color]]:
        #     favorite = 
        favorite = max([x[color]])

    return favorite

def count(x: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in x:
        if item in result:
            result[item] += 1
        else:
            item = 1
    return result