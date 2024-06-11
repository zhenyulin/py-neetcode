from src.string.combination_validate_parentheses import validateParenthesis


def testValidateParenthesis():
    assert validateParenthesis("()") is True
    assert validateParenthesis("(*)") is True
    assert validateParenthesis("((*") is False
    assert validateParenthesis("(*)))") is False
    assert validateParenthesis("(*))") is True
