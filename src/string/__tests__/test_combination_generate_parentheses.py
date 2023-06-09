from src.string.combination_generate_parentheses import generateParentheses


def testGenerateParentheses():
    assert set(generateParentheses(3)) == set(
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    )
    assert generateParentheses(1) == ["()"]
