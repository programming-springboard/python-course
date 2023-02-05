# int_sequence = (1, 2, 3)
#
# # Для послідовности чисел можливо порахувати їх суму функцією sum()
# print("Sum of 1, 2, 3:", sum(int_sequence))
#
# # або знайти максимальне значення функцією max()
# print("Max of 1, 2, 3:", max(int_sequence))
#
# # або мінімальне функцією min
# print("Min of 1, 2, 3:", min(int_sequence))
#
# expressions = (3 > 2, 2 == 2, 1 >= 2)  # (True, True, False)
#
# # Для послідовности значень типу bool можливо зробити перевірку на те, чи є вони
# # всі вірними або чи є з них принаймні одне вірне значення
# print("Are all expressions True? 3 > 2 and 2 == 2 and 1 >= 2)", all(expressions))
# print("Is any of the expressions True?", any(expressions))

str_sequence = ("First", "Second", "Third")
# Будь яку послідовність можна "пронумерувати" функцією enumerate(). Це буває
# корисно у використанні в парі з for-циклом для отримання індексу певного
# елементу
for index, item in enumerate(str_sequence):
    print(f"Sequence item at index {index}: {item}")

# Зверни увагу, що у циклі for вище відбувається присвоєння одразу двох змінних
# Це можливо завдяки особливости роботи Python, що дозволяє присвоювати
# "кортежі" змінних
a, b = (1, 2)
print(f"{a=}; {b=}")
