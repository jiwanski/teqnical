#!/usr/bin/python


def initialize_car():
    return {
        'speed': 0,
        'driver': None,
        'passengers': [],
        'model': None,
        'year': None,
        'color': None,
        'max_passengers': None,
        'configured': False
    }


def set_car_data(car, model, year, max_passengers=5, **kwargs):
    car['model'] = model
    car['year'] = year
    car['max_passengers'] = max_passengers
    if kwargs.get('color'):
        car['color'] = kwargs.get('color')
    car['configured'] = True


def drive(car, speed):
    if not car['driver']:
        print("Cannot drive, there is no driver!")
    else:
        print(f"Starting driving with speed {speed}")


def stop(car):
    car['speed'] = 0


def board_people(car, driver, *passengers):
    car['driver'] = driver
    add_passengers(car, *passengers)


def add_passengers(car, *passengers):
    available = car['max_passengers'] - len(car['passengers'])
    if car['speed'] != 0:
        print("Cannot add passengers while car is moving!")
    elif len(car['passengers']) >= car['max_passengers']:
        print("No free places for new passengers available!'")
    else:
        car['passengers'].extend(passengers[:available])


def describe_car(car) -> None:
    if not car['configured']:
        print('No description for this car is available')
    else:
        description = f'This is {car["model"]} made in {car["year"]}.\n'
        if car["color"]:
            description += f'Color of this car is {car["color"]}\n'
        description += f'Currently the driver is {car["driver"]} and there are {len(car["passengers"])} passengers boarded.\n'
        description += f'Current speed of the car is {car["speed"]}.' if car['speed'] > 0 else 'The car is stopped now.'
        print(description)


if __name__ == '__main__':
    vehicle = initialize_car()
    drive(vehicle, 30)
    set_car_data(vehicle, 'Honda', 1998)
    board_people(vehicle, 'Kate', 'James', 'Nina', 'Mike', 'Bob')
    drive(vehicle, 60)
    describe_car(vehicle)
    add_passengers(vehicle, 'Johnny', 'Betty')
    describe_car(vehicle)
    stop(vehicle)
    add_passengers(vehicle, 'Johnny', 'Betty')
    describe_car(vehicle)
