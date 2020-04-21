# Zadanie 3
heroes = [
    {
        'name': 'Hari Seldon',
        'robot': True,
        'math': 10,
        'history': 4,
        'origin': 'Helicon'
    },
    {
        'name': 'Yugo Amaryl',
        'robot': False,
        'math': 10,
        'history': 1,
        'origin': 'Dahl'
    },
    {
        'name': 'Dors Venabili',
        'robot': True,
        'math': 3,
        'history': 9,
        'origin': 'Cinna'
    },
    {
        'name': 'R. Daneel Olivaw',
        'robot': True,
        'math': 8,
        'history': 10,
        'origin': 'Aurora'
    },
    {
        'name': 'Raych Seldon',
        'robot': False,
        'math': 3,
        'history': 5,
        'origin': 'Dahl'
    },
]

max_avg = 0
nerd = None

for hero in heroes:
    scores = [hero['math'], hero['history']]
    avg = sum(scores) / len(scores)
    if avg > max_avg:
        max_avg = avg
        nerd = hero['name']

print(f"This nerd, {nerd}, has maximum average score of {max_avg}")
# auto challenge
is_nerd_robot = int([h['robot'] for h in heroes if h['name'] == nerd][0])
print(f"But he is{[' not', ''][is_nerd_robot]} a robot!")
