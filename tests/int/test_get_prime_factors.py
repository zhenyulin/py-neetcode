from src.int.get_prime_factors import primeFactors


def testPrimeFactors():
    assert primeFactors(84) == [2, 2, 3, 7]
    assert primeFactors(99) == [3, 3, 11]
