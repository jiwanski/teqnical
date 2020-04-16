# zadanie 3

"""
Stwórz słownik opisujący ulubiony zespół (albo jakikolwiek zespół), który zawiera następujące klucze:
  * name - nazwa zespołu
  * country – kraj pochodzenia
  * albums – lista tytułów albumów
  * start_year - rok rozpoczęcia działalności
  * albums_sold – liczba sprzedanych albumów
"""
band = {
    'name': 'Egypt',
    'country': 'USA',
    'albums': ['Egypt', 'Become The Sun', 'Endless Flight'],
    'start_year': 2003,
    'albums_sold': 15927
}

# Dodaj do słownika nowy klucz: active – opisujący czy zespół jest aktywny (prawda/fałsz)
band['active'] = False

# Dodaj do klucza albums nowy album na koniec listy
band['albums'].append('Cracks And Lines')

# Wydrukuj wszystkie albumy
print(*band['albums'], sep=', ')

# Zmien wartość active na przeciwną
band['active'] = not band['active']

# Zwiększ wartość sprzedanych albumów o 1 (gratuluję zakupu!)
band['albums_sold'] += 1

print(band)
