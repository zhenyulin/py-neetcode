#
# Visiting Cities
#
# There are a number of cities in a row, and there are two bus lines that go between them.
# Starting on  or moving to Blue Line takes extra time, but not for Red Line.
# Find the minimum cost to move from the first city to each of the cities.
#
# Example:
# red = [2,3,4]
# blue = [3,1,1]
# blueCost = 2
#
# For 4 cities, times from City 0 to i(1,2,3) are noted as red[i-1], blue[i-1]
# the answer would be [0,2,5,6]
#
# Constaints:
# return int[n], 2 <= 2 <= 2*10^5
# 1 <= red[i], blue[i], blueCost <= 10^9
#


def minCost(red: list[int], blue: list[int], blue_cost: int) -> list[int]:
    """
    1) Dynamic Programming

    at each dp[i], it can be from_red or from_blue
    so we need to record the mins to each from_red, from_blue too

    time complexity: O(N), space complexity: O(1)
    """

    res, from_red, from_blue = [0], 0, blue_cost

    for i in range(len(red)):
        to_red = min(from_red + red[i], from_blue + red[i])
        to_blue = min(from_red + blue[i] + blue_cost, from_blue + blue[i])
        res.append(min(to_red, to_blue))
        from_red, from_blue = to_red, to_blue

    return res
