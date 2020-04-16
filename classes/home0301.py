# zadanie 1

# Zdefiniuj listę “primes” zawierającą 10 kolejnych liczb pierwszych zaczynając od
primes = [2, 3, 5, 7, 11, 13, 15, 17, 23, 29]

# Wydrukuj długość tej listy
list_len = len(primes)
print(list_len)

# Dodaj na koniec listy 11tą liczbę pierwszą
primes.append(31)
primes_last_element = primes[-1]

# Stwórz drugą listę “primes_four” zawierającą pierwsze 4 elementy “primes”
primes_four = primes[0:4]

# Wydrukuj ostatni z elementów “primes_four”
primes_four_last = primes_four[-1]
print(primes_four_last)

"""
Używając funkcji sum() policz sumę “primes” i “primes_four”. 
Ile razy większa jest suma “primes” od “primes_four”?
"""
primes_ratio = sum(primes) // sum(primes_four)
print(primes_ratio)
