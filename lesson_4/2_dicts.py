# Ще одним мутабельним (змінюваним) типом даних в Python є словники, або dict
# (скорочення від dictionary).

# Елементи словника ініціалізуються в фігурних дужках {}. Елементами словника
# є пари ключ-значення. Ключами словника можуть бути будь-які незмінювані типи
# даних (числа, строки, кортежі). Значеннями словника можуть бути будь-які
# типи даних.
my_dict = {
    "my_key": "my_value",
    "another_key": 42,
    42: "another_value",
}
print("my_dict:", my_dict)
print("type of my_dict", type(my_dict))

# Отримання значення зі словника відбувається за ключем. Для отримання значення
# необхідно передати ключ до квадратних дужок, подібно до того, як елементи
# списку отримуються за індексом
print('my_dict value by key "my_key":', my_dict["my_key"])
print('my_dict value by key 42:', my_dict[42])

# Оскільки dict є змінним типом даних, його значення можна модифікувати за
# ключем
my_dict["my_key"] = "my_new_value"
print('my_dict value by key "my_key":', my_dict["my_key"])

# або ж додавати нові пари ключ-значення до dict
my_dict["my_new_key42"] = "brand_new_value"
print("my_dict after modification:", my_dict)

# Елементами dict можуть бути як tuple, list так і інший dict
another_dict = {
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {
        7: "seven",
        8: "eight",
        9: "nine",
    }
}
print("another_dict:", another_dict)

# Для отримання значення з dict можна використовувати також метод .get()
# Його перевагою є те, що в разі, якщо даного ключа нема в dict - то він
# поверне None, або значення, передане другим аргументом до .get()
print('my_dict value by key "my_key"', my_dict.get("my_key"))
print('my_dict value by key "missing_key"', my_dict.get("missing_key"))
print('my_dict value by key "missing_key42"', my_dict.get("missing_key42", 42))

# Для того, аби видалити значення з dict необхідно використати метод .pop()
# Метод .pop() в результаті свого виконання повертає значення
popped_value = my_dict.pop("my_new_key_42")
print('my_dict after .pop():', my_dict)
print("popped value is", popped_value)

# Для того, аби отримати всі ключі dict необхідно використати метод .keys()
print("my_dict keys:", my_dict.keys())

# Ітеруючись по dict, ми будемо ітеруватись саме по ключам:
print("my_dict keys line by line")
for key in my_dict:
    print(key)

# Використовуючи останню властивість dict, можна також перевірити наявність
# певного ключу всередині нього за допомогою ключового слова in
if "my_key" in my_dict:
    print('"my_key" key is presented in my_dict')
else:
    print('"my_key" key is not presented in my_dict')

# Для того, аби отримати всі значення dict необхідно використати метод
# .values()
print("my_dict values:", my_dict.values())

# Для того, аби отримати всі пари ключ-значення у вигляді списку кортежів
# необхідно використати метод .items()
print("my_dict key-value pairs", my_dict.items())

# Використовуючи останній метод, можна проітеруватись по елементах dict
print("my_dict key-value pairs line by line")
for key, value in my_dict.items():
    print(f"{key}: {value}")
