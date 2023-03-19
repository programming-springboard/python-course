"""Цей модуль містить в собі функцію для розбиття числа на цифри."""


def get_digits(num):
    """Розбити надане додатне число на цифри.

    :param num: Вхідне число, яке треба розбити на цифри.
    :type num: int

    :raises ValueError: Якщо надане число менше нуля.

    :return: Список цифр, що вони були в наданому числі.
    :rtype: list
    """
    if num < 0:
        raise ValueError("The given number must be greater than zero")
    if num < 10:
        return [num]
    else:
        return get_digits(num // 10) + [num % 10]
