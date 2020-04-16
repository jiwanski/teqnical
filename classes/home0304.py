# zadanie 4

# W zmiennej “bands” stwórz listę 3 zespołów opisanych słownikami z zadania 3
band1 = {'name': 'Mother Engine', 'country': 'Germany', 'albums': ['Muttermaschine', 'Absturz', 'Hangar'],
         'start_year': 1988, 'albums_sold': 13492, 'active': True}
band2 = {'name': 'Egypt', 'country': 'USA', 'albums': ['Egypt', 'Become The Sun', 'Endless Flight'], 'start_year': 2003,
         'albums_sold': 15927, 'active': False}
band3 = {'name': 'Stoned Jesus', 'country': 'Ukraine',
         'albums': ['First Communion', 'Seven Thunders Roar', 'The Harvest', 'Pilgrims'], 'start_year': 1996,
         'albums_sold': 202981, 'active': True}

bands = [band1, band2, band3]

# Wydrukuj kraj pochodzenia ostatniego zespołu
bandlast_country = bands[-1]['country']
print(bandlast_country)

# Wydrukuj pierwszy album drugiego zespołu
band2_album1 = bands[1]['albums'][0]
print(band2_album1)

# Wydrukuj stan aktywności (klucz “active”) pierwszego zespołu
band1_active = bands[0]['active']
print(band1_active)
