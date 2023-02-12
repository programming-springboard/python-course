my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("my_list values", my_list)

# В списка можна отримати індекс елемента, за його значенням:
print("Index of element with value 21:", my_list.index(21))

# В списка можна отримати кількість входжень певних значень
print("Count of elements with value 1:", my_list.count(1))
print("Count of elements with value 21:", my_list.count(21))

# Зі списка можна викинути останній елемент:
my_list.pop()  # виконання цього методу модифікує список!
print("my_list items after calling .pop():", my_list)

# Список можна "відзеркалити":
my_list.reverse()  # виконання цього методу модифікує список!
print("my_list items after calling .reverse()", my_list)

# Елементи списку можна також відсортувати
my_list.sort()
print("my_list items after calling .sort()", my_list)

# Більше методів - в документації
# https://www.w3schools.com/python/python_ref_list.asp
