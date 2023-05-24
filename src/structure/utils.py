from typing import Callable


def binary_search_index(
    sequence: list, value: any, key: Callable = lambda x: x, ascending: bool = True
):
    """
    use binary search when the relationship between value and elements in the sequence is binary
    and the elements have certain order based on the value
    """
    i, j = 0, len(sequence)

    while i < j:
        m = (i + j) // 2
        # { on the left, move the left closer }
        if (not ascending) ^ (
            key(sequence[m]) <= value
        ):  # use <= if prefer to append to the right
            i = m + 1  # use + 1 to try meet the left condition
        else:
            j = m

    return i
