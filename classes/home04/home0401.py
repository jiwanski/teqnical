import math
import random
from datetime import datetime
from pprint import pprint

# Listy zawierające dane do losowania
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

# Przykład jak można losować imię z listy
random_female_firstname = random.choice(female_fnames)
# print(random_female_firstname)

# Przykład jak można losować wiek z liczb całkowitych od 1 do 65
random_age = random.randint(1, 65)
# print(random_age)

# Przykładowy wygenerowany pojedynczy słownik
example_dictionary = {
    'firstname': 'Kate',
    'lastname': 'Yu',
    'email': 'kate.yu@example.com',
    'age': 23,
    'country': 'Poland',
    'adult': True,
    'birth_year': 1980
}

# ROZWIĄZANIE

# wielkość zbioru generowanych osób
group = 40
# po ile mężczyzn i kobiet - uwaga - przy grupach nieparzystych różnica NIE JEST losowa
males = round(group / 2)
females = group - males
# losowe listy o wielkości wyznaczonej przez zmienna group
rnd_firstnames = random.choices(female_fnames, k=females) + random.choices(male_fnames, k=males)
random.shuffle(rnd_firstnames)
rnd_countries = random.choices(countries, k=group)
rnd_surnames = random.choices(surnames, k=group)
rnd_ages = random.choices(range(5, 45), k=group)
# current year
year = datetime.now().year
# inicjalizacja listy słowników
people = []

for i in range(group):
    # statyczne wartości - aby uniknąć person = {} i od razu utworzyć słownik
    person = {
        'age': rnd_ages[i],
        'country': rnd_countries[i],
        'firstname': rnd_firstnames[i],
        'lastname': rnd_surnames[i]
    }
    # dynamiczne wartości - na bazie już istniejącego słownika
    person['adult'] = person['age'] >= 18
    person['email'] = f"{person['firstname'].lower()}.{person['lastname'].lower()}@example.com"
    person['birth_year'] = year - person['age']
    # dodaj ostateczny słownik do listy
    people.append(person)

for i, p in enumerate(people):
    print(f"({i + 1}) "
          f"Hi! I'm {p['firstname']} {p['lastname']}. "
          f"I come from {(p['country'], 'planet Earth')[p['country'] == 'Other']} "
          f"and I was born in {p['birth_year']}")
