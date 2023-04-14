from src.string.substring_count_equal_one_split import numWays


def testNumWays():
    assert numWays("10101") == 4
    assert numWays("1001") == 0
    assert numWays("0000") == 3
