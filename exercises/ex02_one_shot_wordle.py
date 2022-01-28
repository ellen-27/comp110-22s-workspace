"""EX02 - One Shot Wordle."""

__author__ = "730331514"

secret: str = "python"
index: int = 0
emoji: str = ""
present: bool = False
alt: int = 0

guess = input(str("What is your 6-letter guess? "))

while len(guess) != len(secret):
    guess = input("That was not 6 letters! Try again: ")

while index < len(secret):
    if secret[index] == guess[index]:
        emoji = emoji + "\U0001F7E9"
    else:
        while present is False and alt < len(secret):
            if guess[index] == secret[alt]:
                present = True
            else:
                alt = alt + 1
        if present is True:
            emoji = emoji + "\U0001F7E8"
            present = False
        else:
            emoji = emoji + "\U00002B1C"
        alt = 0
    index = index + 1

print(emoji)

if len(guess) == len(secret) and guess != secret:
    print("Not quite. Play again soon!")
    quit()

if guess == secret:
    print("Woo! You got it!")
    quit()