# Іншим типом даних для збереження переліків даних є множини (англ. set)
# Вони є імплементацією поняття з теорії множин
# https://uk.wikipedia.org/wiki/Теорія_множин

# Ініціалізація множин відбувається у фігурних дужках {}
# Елементи множин не можуть повторюватись
# Елементами множин можуть бути лише незмінювані типи даних (числа, строки або
# кортежі)
first_set = {1, 2, 3, 4, 4, 4, 4, 4}
second_set = {3, 4, 5, 6}
print("type of first_set:", type(first_set))
print("first_set:", first_set)
print("second_set:", second_set)

# Над множинами можна проводити різні операції з теорії множин

# Для отримання обʼєднання двох множин використовується оператор |
print("set union:", first_set | second_set)

# Для отримання перетину двох множин використовується оператор &
print("set intersection", first_set & second_set)

# Для отримання різниці двох множин використовується оператор -
print("set difference", first_set - second_set)
print("set difference (other)", second_set - first_set)

# Для отриманя симетричної різниці двох множин використовується оператор ^
print("set symmetric difference", first_set ^ second_set)

# Для визначення того, чи є одна множина підмножиною другої використовується
# метод .issubset()
first_set = {1, 2}
second_set = {1, 2, 3, 4, 5, 6}
print("is first set a subset of second set?", first_set.issubset(second_set))

# set - це змінюваний тип даних. В Python також є аналог set, що є незмінюваним
# це frozenset
my_frozenset = frozenset([1, 2, 3, 4])
print("type of my_frozenset", type(my_frozenset))
print("my_frozenset", my_frozenset)
