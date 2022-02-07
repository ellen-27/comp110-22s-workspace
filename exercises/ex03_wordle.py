"""Exercise 3: Wordle but Structured."""

__author__ = "730331514"

def contains_char(long: str, one: str) -> bool:
    """Indicates if single character is found in given string"""
    assert len(one) == 1
    index: int = 0
    alt: int = 0
    while index < len(long):
        if one == long[index]:
            index += 1
            return True
        else:
            index: int = index + 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Will return an emoji string that reflects likeness of two given strings"""
    assert len(guess) == len(secret)
    i: int = 0
    emojis: str = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            emojis += "\U0001F7E9"
        else:
            if contains_char(secret, guess[i]) == False:
                emojis += "\U00002B1C"
            else:
                emojis += "\U0001F7E8"
        i += 1
    return emojis