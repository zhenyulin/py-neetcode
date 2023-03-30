from src.array.letter_combinations_of_a_phone_number import letterCombinations


def testLetterCombinations():
    assert letterCombinations("") == []
    assert set(letterCombinations("2")) == set(["a", "b", "c"])
    assert set(letterCombinations("23")) == set(
        [
            "ad",
            "ae",
            "af",
            "bd",
            "be",
            "bf",
            "cd",
            "ce",
            "cf",
        ]
    )
