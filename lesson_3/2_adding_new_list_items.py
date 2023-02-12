# Для ініціалізації пустого списку необхідно вказати пусті квадартні дужки []
my_list = []
print("my_list is now empty:", my_list)

# Для додавання нових елементів до списку, необхідно скористатись
# методом .append(), передавши туди аргументом значення нового елемента, що
# буде додано в кінець

# * Методи - це функції, призначені для якогось конкретного типу даних. Для
#   виклику методу, наобхідно поставити точку після змінної певного типу даних,
#   після цього вказати назву методу і круглі дужки (), так само як і під час
#   виклику функцій.
my_list.append("First element")
print("my_list items after first .append() call:", my_list)

my_list.append("Second element")
print("my_list items after second .append() call:", my_list)

# Додавати нові елементи до списку можна також по декілька за раз. Для цього
# необхідно скористатись методом .extend(), передавщи йому в якості аргумента
# інший список
other_list = ["Third element", "Fourth element"]
print("Values of other_list", other_list)

my_list.extend(other_list)
print("Values of my_list after extending it with other_list values:", my_list)
