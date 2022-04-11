from __future__ import annotations


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str) -> StrArray:
        """vectorized concatenation operator."""
        result: list[str] = []
    # set up a result list of strings that's empty
    # loop thru each item in self.items
    # for each item, append the concatenation of item and rhs to result list
    # return a newly constructed StrArray whose items are result
        for item in self.items:
            result.append(item + rhs)

        return StrArray(result)
         

first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
# print(first + last)