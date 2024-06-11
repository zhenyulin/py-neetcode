from src.tree.path_sum_max import maxPathSum


def testMaxPathSum():
    maxPathSum([1, 2, 3]) == 6
    maxPathSum([-10, 9, 20, None, None, 15, 7]) == 42
