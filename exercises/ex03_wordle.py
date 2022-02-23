"""Exercise 3: Wordle but Structured."""

__author__ = "730331514"


def contains_char(long: str, one: str) -> bool:  # if 'one' is found in 'long', this returns True 
    """Indicates if single character is found in given string."""
    assert len(one) == 1
    index: int = 0
    while index < len(long):
        if one == long[index]:
            index += 1
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:  # if indices match, returns green emoji; if contains_char returns False, return white, but if not False, return yellow 
    """Will return an emoji string that reflects likeness of two given strings."""
    assert len(guess) == len(secret)
    i: int = 0
    emojis: str = ""
    while i < len(secret):
        if secret[i] == guess[i]:
            emojis += "\U0001F7E9"
        else:
            if not contains_char(secret, guess[i]):
                emojis += "\U00002B1C"
            else:
                emojis += "\U0001F7E8"
        i += 1
    return emojis


def input_guess(length: int) -> str:  # while the length of word is not equal to input, input again but otherwise return the word
    """Returns user's guess of provided length."""
    i = length
    word = input(f'Enter a {i} character word: ')
    while len(word) != length:
        word = input(f"That wasn't {i} chars! Try again: ")
    return word


def main() -> None:  # main function - turns, f-strings, booleans, variables... 
    """The entrypoint of the program and main game loop."""
    main_secret: str = "codes"
    turns: int = 1
    won: bool = False
    while turns < 7:
        print(f"=== Turn {turns}/6 ===")
        main_guess = input_guess(5)
        print(f"{emojified(main_guess, main_secret)}")
        if main_guess == main_secret:
            print(f"You won in {turns}/6 turns!")
            turns = 7
            won = True
        turns += 1
    if not won: 
        print("X/6 - Sorry, try again tomorrow!") 


if __name__ == "__main__": 
    main()