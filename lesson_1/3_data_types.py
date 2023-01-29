# Python - динамічно типізована мова програмування. Це означає, що він сам
# автоматично визначає тип змінної, в залежності від значення, з яким вона була
# ініціалізована.

my_string_variable = "A text of any possible length"  # змінна типу str
my_integer_variable = 42  # змінна типу int
my_floating_point_number_variable = 12.5  # змінна типу float

print("My string variable value:", my_string_variable)
print("My integer variable value:", my_integer_variable)
print("My floating point number value:", my_floating_point_number_variable, end="\n\n")

# За допомогою функції type() можна дізнатись, якого типу даних є змінна

# Зверни увагу, що не обовʼязково зберігати результат виконання type() в
# окрему змінну, аби потім вивести її на екран. Можна викликати її "всередині"
# функції print(). В такому випадку, спочатку завершить своє виконання функція
# type() і результат її виконання буде передано як аргумент функції print().

# print("My string variable type:", type(my_string_variable))
# print("My integer variable type:", type(my_integer_variable))
# print("My floating point number variable type:", type(my_floating_point_number_variable))
