"""Example of a functin that searches through at list."""


def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))
    
# Define a function named contains
# Two parameters:
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #  for each item in the haystack
    #   test if it is equal to the needle
    #       if so, return True
    for item in haystack:
        if item == needle:
            return True
    return False

if __name__ == "main":
    main()
