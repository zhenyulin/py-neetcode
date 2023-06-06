from src.string.splits_char_unique_part import partitionLengthes


def testPartitionLengthes():
    assert partitionLengthes("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partitionLengthes("eccbbbbdec") == [10]
