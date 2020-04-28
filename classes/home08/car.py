class Car:

    def __init__(self, driver=None, model=None, year=None, color=None, max_passengers=None, passengers=[], speed=0,
                 configured=False):
        self.passengers = passengers
        self.speed = speed,
        self.driver = driver,
        self.passengers = passengers,
        self.model = model,
        self.year = year,
        self.color = color,
        self.max_passengers = max_passengers,
        self.configured = configured

    def set_car_data(self, model, year, max_passengers=5, **kwargs):
        self.model = model
        self.year = year
        self.max_passengers = max_passengers
        if kwargs.get('color'):
            self.color = kwargs.get('color')
        self.configured = True

    def drive(self, speed):
        if not self.driver:
            print("Cannot drive, there is no driver!")
        else:
            print(f"Starting driving with speed {speed}")
            self.speed = speed

    def stop(self):
        self.speed = 0

    def board_people(self, driver, *passengers):
        self.driver = driver
        self.add_passengers(*passengers)

    def add_passengers(self, *passengers):
        available = self.max_passengers - len(self.passengers)
        print(available)
        if self.speed != 0:
            print("Cannot add passengers while car is moving!")
        elif not available > 0:
            print("No free places for new passengers available!'")
        else:
            self.passengers.extend(passengers[:available])

    def describe_car(self):
        description = ''
        if not self.configured:
            print('No description for this car is available')
        else:
            description = f'This is {self.model} made in {self.year}.\n'
            if self.color is not None:
                description += f'Color of this car is {self.color}\n'
            description += f'Currently the driver is {self.driver} and there are {len(self.passengers)} passengers ' \
                           f'boarded.\n '
            description += f'Current speed of the car is {self.speed}.' if self.speed > 0 else 'The car is stopped now.'
        print(description)


vehicle = Car()
vehicle.drive(30)
vehicle.set_car_data('Honda', 1998)
vehicle.board_people('Kate', 'James', 'Nina', 'Mike', 'Bob')
vehicle.drive(60)
vehicle.describe_car()
vehicle.add_passengers('Johnny', 'Betty')
vehicle.describe_car()
vehicle.stop()
vehicle.add_passengers('Johnny', 'Betty')
vehicle.describe_car()
