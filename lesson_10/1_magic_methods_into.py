# Магічні методи - це спеціальні методи з підкресленням на початку та в кінці
# назви, які можна перевизначати в класах Python. Ці методи дозволяють
# визначати поведінку класу під час виконання різних операцій, таких як
# додавання, віднімання, порівняння, створення екземплярів та інші.
# Використовуючи магічні методи, ми можемо створювати більш зрозумілі та
# ефективні класи.

class Car(object):  # всі класи в Python є нащадками класу object по дефолту
    def __init__(self, brand, model, year):
        """
        Магічний метод init використовується для констроювання обʼєкту класу.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        """
        Магічний метод str використовується для визначення строкової
        """
        return f"{self.brand} {self.model} ({self.year})"

    def __eq__(self, other):
        """
        Магічний метод eq використовується для перевірки двох обʼєктів класу
        на рівність між собою.
        """
        if not isinstance(other, Car):
            raise TypeError("You can only compare car to other car")
        return self.brand == other.brand and self.model == other.model


if __name__ == "__main__":
    car = Car("Volkswagen", "Golf", 2011)
    car2 = Car("Daewoo", "Lanos", 2001)
    print("The car is", str(car))

    # str(car)   # викличеться car.__str__()
    # car == car2   # викличеться car.__eq__(car2)
