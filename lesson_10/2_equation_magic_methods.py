class Distance:
    def __init__(self, ft, inch):
        self.ft = ft
        self.inch = inch

    def __eq__(self, other):
        return self.to_cm() == other.to_cm()

    def __gt__(self, other):
        return self.to_cm() > other.to_cm()

    def __ge__(self, other):
        return self.to_cm() >= other.to_cm()

    def to_cm(self):
        return self.ft * 12 + self.inch


if __name__ == "__main__":
    d1 = Distance(1, 5)
    d2 = Distance(2, 1)

    print("d1 > d2 =", d1 > d2)
    print("d1 <= d2 =", d1 <= d2)
    print("d1 != d2", d1 != d2)
