from prime_generator import PrimeGenerator


def test_constructor():
    """Test the constructor"""
    pg = PrimeGenerator()
    assert pg.primes == []
    assert pg.composites == set()


def test_prime_to_max():
    """Test the prime generator method"""
    pg1 = PrimeGenerator()
    pg2 = PrimeGenerator()
    pg3 = PrimeGenerator()
    prime_list1 = [2, 3, 5, 7]
    prime_list2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    prime_list3 = [2, 3, 5, 7, 11, 13, 17, 19]
    assert pg1.prime_to_max(10) == prime_list1
    assert pg2.prime_to_max(45) == prime_list2
    assert pg3.prime_to_max(20) == prime_list3
