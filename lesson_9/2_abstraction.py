class RacingCar:
    def __init__(self, name):
        self.name = name

        self.distance = 0
        self.race = None

    def bind_to(self, race):
        self.race = race

    def move(self, distance):
        if distance > 0:
            self.distance += distance
        else:
            raise ValueError("A distance must be greater than 0")

    def get_position_in_race(self):
        if self.race is None:
            raise ValueError("A car is not in any race")
        return self.race.get_car_position(self)


class Race:
    def __init__(self, cars):
        self.cars = cars

        for car in self.cars:
            car.bind_to(self)

    def get_car_position(self, car):
        cars_sorted_by_distance = sorted(self.cars, key=lambda c: c.distance, reverse=True)

        for position, race_car in enumerate(cars_sorted_by_distance, start=1):
            if race_car is car:
                return position
        else:
            raise ValueError("A car is not within the race")


if __name__ == "__main__":
    car1 = RacingCar(name="Ferrari")
    car2 = RacingCar(name="Aston Martin")
    car3 = RacingCar(name="McLaren")

    race = Race(cars=[car1, car2, car3])

    car1.move(30)
    car2.move(20)
    car3.move(40)

    for car in (car1, car2, car3):
        print(f'The position of "{car.name}" car in race is {car.get_position_in_race()}')
