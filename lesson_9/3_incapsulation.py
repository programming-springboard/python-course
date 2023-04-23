class RacingCar:
    def __init__(self, name):
        self.name = name
        self._distance = 0

    def move(self, distance):
        if distance > 0:
            self._distance += distance
        else:
            raise ValueError("A distance must be greater than 0")

    def is_at_point(self, destination_point):
        return self._distance >= destination_point


if __name__ == "__main__":
    car = RacingCar("Aston Martin")
    print(car.name)  # ok
    print(car._distance)  # not ok
