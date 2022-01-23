"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730331514"


five_chr_word: str = input("Enter a 5-character word: ")

if len(five_chr_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Character must be a single character.")
    quit()

match = 0

print("Searching for " + single_character + " in " + five_chr_word)

if single_character == five_chr_word[0]:
    print(single_character + " found at index 0")
    match = match + 1

if  single_character == five_chr_word[1]:
    print(single_character + " found at index 1")
    match = match + 1

if single_character == five_chr_word[2]:
    print(single_character + " found at index 2")
    match = match + 1

if single_character == five_chr_word[3]:
    print(single_character + " found at index 3")
    match = match + 1

if single_character == five_chr_word[4]:
    print(single_character + " found at index 4")
    match = match + 1

if match == int(2):
    print("2 instances of " + single_character + " in " + five_chr_word)

if match == int(1):
    print("1 instance of " + single_character + " in " + five_chr_word)

if match == int(0):
    print("No instances of " + single_character + " in " + five_chr_word)

