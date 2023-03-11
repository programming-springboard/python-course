# x = int(input("Give me a number: "))
#
# if not isinstance(x, (str, bytes, int, float)):
#     raise TypeError(f"int() argument must be a string, a bytes-like object or a real number, not '{type(x)}'")
#
# if x < 0:
#     raise ValueError("The number could not be lower than 0")

try:
    raise TypeError("A type error")
except TypeError as error:  # error = TypeError("A type error")
    print("Type error caught:", error)


### Завдання на занятті ###

# 1. Написати програму, що буде запитувати в користувача число 'x' і виводити
#    до консолі результат виразу `1/x`. У випадку, коли така операція
#    неможлива, виводити до консолі повідомлення "така операція неможлива".

# 2. Модифікувати попередню програму наступним чином: програма буде запитувати
#    в користувача ввести число `x` доти, доки він не введе валідне число,
#    значення якого не менше за нуль. В кінці виконання програми виводити на
#    екран кількість спроб, що їх було здійснено користувачем до того, як
#    програма вдало завершила своє виконання. В кінці кожної спроби виводити
#    до консолі повідомлення з номером поточної спроби.
