class Car:
    def __init__(self, name):
        self.name = name
        self._distance = 0

    def move(self, distance):
        if distance > 0:
            self._distance += distance
        else:
            raise ValueError("A distance must be greater than 0")


class RacingCar(Car):
    def __init__(self, name):
        super().__init__(name)
        self._race = None

    def bind_to(self, race):
        self._race = race

    def get_position_in_race(self):
        if self._race is None:
            raise ValueError("A car is not in any race")
        return self._race.get_car_position(self)
