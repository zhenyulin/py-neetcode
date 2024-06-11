from src.string.splits_count_equal_num_char import numWays


def testNumWays():
    assert numWays("10101") == 4
    assert numWays("1001") == 0
    assert numWays("0000") == 3
