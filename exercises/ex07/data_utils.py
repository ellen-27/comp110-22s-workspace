"""Dictionary related utility functions."""

__author__ = "730331514"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read entire CSV of data into a list of rows, with each row represented as a dictionary."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close() 
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a dictionary of columns."""
    result: dict[str, list[str]] = dict()
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)  
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data."""
    result: dict[str, list[str]] = dict()
    for column in table:
        first_row: list[str] = []
        i: int = 0
        if len(table[column]) < n:
            result[column] = table[column]
        else:
            while i < n:
                first_row.append(table[column][i])
                i += 1
            result[column] = first_row

    return result


def select(x: dict[str, list[str]], y: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = dict()
    for column in y:
        result[column] = x[column]
    return result


def concat(x: dict[str, list[str]], y: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table wtih two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in x:
        result[column] = x[column]
    for column in y:
        if column in result:
            result[column] += y[column]
        else:
            result[column] = y[column]    
    return result


def count(x: list[str]) -> dict[str, int]:
    """Produces a dictionary where each key is counted for in the input list."""
    result: dict[str, int] = {}
    for item in x:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result