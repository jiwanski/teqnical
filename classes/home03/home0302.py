# zadanie 2

# zapisz do zmiennej listę [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
some_list = [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]

# używając funkcji sorted() przypisz do innej zmiennej posortowaną listę z pierwszego punktu
list_sorted = sorted(some_list)
some_list.sort()

# wydrukuj pierwszy i ostatni element nowej listy
first, last = list_sorted[0], list_sorted[-1]
print(first, last)
