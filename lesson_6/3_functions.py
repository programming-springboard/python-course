# Функції в процедурному програмуванні використовуються для визначення
# повторюваних блоків коду.

# Функція визначається наступним чином: def <назва функцію(перелік аргументів);
# Функція може приймати довільне число аргументів (в тому числі і 0).
# В результаті свого виконання функція також може повертати результат.
# За замовчуванням всі функції повертають None
def add(a, b):
    return a + b


def print_addition_result(result):
    print("The addition result is", result)
    # return None    or just     return


result_1 = add(2, 2)
# result_1 = add(a=2, b=2)
# result_1 = add(2, b=2)
result_2 = print_addition_result(result_1)


print("First function result", result_1)
print("Type of first function result", type(result_1))

print("Second function result", result_2)
print("Type of second function result", type(result_2))
