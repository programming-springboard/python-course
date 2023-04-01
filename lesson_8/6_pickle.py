import pickle

from decimal import Decimal


obj = Decimal("0.12138")

with open("file.pickle", "wb") as file:
    pickle.dump(obj, file)
