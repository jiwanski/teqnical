from classes import home0302 as home


def test_sorted_list():
    assert home.list_sorted == [-444, -120, -2, 0.0, 0, 3.3, 5, 22, 35, 42, 69.9, 123, 701]


def test_first_element():
    assert home.first == -444


def test_last_element():
    assert home.last == 701
