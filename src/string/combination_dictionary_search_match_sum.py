#
# 1307. Verbal Arithmetic Puzzle
# https://leetcode.com/problems/verbal-arithmetic-puzzle/description/
#


def isSolvable(words: list[str], result: str) -> bool:
    """

    1) DFS

    search the possible value map from last digit and on wards
    lazily assign value to char only until come across new char
    end the current value map sequence if didn't match on one digit

    time complexity: O(), space complexity: O()
    """

    if max(map(len, words)) > len(result):
        return False

    # to assign values to 'result' chars lazily, 'result' is appended to 'words'
    # so carry value would be deducted instead of added at the last index
    _words = [*words, result]
    digits, values = [False] * 10, {}

    # to assign value to individual char lazily, we will do DFS word by word from lower digit
    # since we need conditional resursion, we will search (w, i) together so that DFS returns bool
    def dfs(w: int, i: int, val: int) -> bool:
        """search possible value map at 'i' digit at word 'w' with 'val' value"""

        # { target condition }
        # finished search last digit in result
        if i == len(result):
            return val == 0

        # finished all words, search next digit
        if w == len(_words):
            carry, current = divmod(val, 10)
            return current == 0 and dfs(0, i + 1, carry)

        # skip if the current word isn't long enough
        if i >= len(_words[w]):
            return dfs(w + 1, i, val)

        c = _words[w][~i]
        if c not in values:
            # assign the next valid value continue search
            for n, used in enumerate(digits):
                # no leading zero - not (i == len(_words[w]) - 1 and i != 0 and digit == 0)
                if not used and (n or i == 0 or i < len(_words[w]) - 1):
                    values[c], digits[n] = n, True
                    if dfs(w, i, val):
                        return True
                    # free up the value, as soon as the branch didn't work
                    digits[n] = False
                    values.pop(c)
        else:
            # in case of leading 0
            # assign 0 to non-leading char can create leading 0 elsewhere
            if i and i == len(_words[w]) - 1 and values[c] == 0:
                return False
            # if the current word is result, deduct the digit
            return dfs(
                w + 1, i, val + (values[c] if w < len(_words) - 1 else -values[c])
            )

    return dfs(0, 0, 0) is True
