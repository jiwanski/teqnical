# task 1
def points_distance(position_1: list, position_2: list) -> float:
    xy_diff = [abs(x - y) for x, y in zip(position_1, position_2)]
    distance = (xy_diff[0] ** 2 + xy_diff[1] ** 2) ** 0.5
    return round(distance, 2)


# task 2
def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight / height ** 2
    return round(bmi, 2)


# task 3
def status_bmi(bmi: float) -> str:
    thresholds = [18.5, 25, 30]
    diagnoses = ['niedowaga', 'optimum', 'nadwaga', 'otyłość']
    for t in thresholds:
        if bmi < t:
            return diagnoses[thresholds.index(t)]
    return diagnoses[-1]


# task 4
def check_bmi() -> str:
    weight = float(input("waga? "))
    height = float(input("wzrost? "))
    return status_bmi(calculate_bmi(weight, height))
