from classes.home03 import home0301 as home


def test_list_length():
    assert home.list_len == 10


def test_sublist():
    assert home.primes_four == [2, 3, 5, 7]


def test_primes_last_element():
    assert home.primes_last_element == 31


def test_primes_four_last_element():
    assert home.primes_four_last == 7


def test_sum_ratio():
    assert home.primes_ratio == 9
