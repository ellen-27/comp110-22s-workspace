"""Dictionary exercise."""

__author__ = "730331514"

def invert(x: dict[str, str]) -> dict[str,str]:
    """Inverts the keys and values."""
    # y: dict[str, str] = {}
    for key in x:
        x.pop(key)
        x[(x[key])] = x[key]
        # y[key] = key
    return x

def favorite_color(x: dict[str, str]) -> str:
    