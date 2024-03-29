# Рекурсія - це процес виклику функції, яка знову викликає себе саму, зазвичай
# з іншими аргументами, для обчислення результату. Це може продовжуватися
# доти, доки не буде досягнуто базового випадку, коли функція викликає себе з
# аргументами, що не потребують додаткових викликів функції. Базовий випадок
# є необхідним, щоб уникнути нескінченного циклу рекурсії.

# У програмуванні, рекурсія часто використовується для розв'язання складних
# задач, таких як сортування, пошук та обробка даних. Використання рекурсії
# дозволяє спростити і скоротити код, а також зробити його більш читабельним
# і зрозумілим. Однак, необхідно бути обережним при використанні рекурсії, щоб
# уникнути переповнення стеку і зайвого споживання пам'яті.


def get_digits(num):
    """Це - текстова документація до функції або docstring.

    Docstring використовується для пояснення коду, аби іншим розробникам було
    легше розібратись з призначенням функції. Як правило, docstring складається
    з короткого опису в першому рядку, що доповнено детальним описом з нового
    абзацу (якщо треба). Далі можливо описати всі параметри, що приймає
    функція, помилки, що вона викидає, а також значення, що вона повертає.

    Дана функція призначена для розбиття наданого додатного числа на цифри.

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


def fibonacci(n):
    """Розрахувати число Фібоначчі за заданою індексом (порядковим номером).

    :param n: Індекс числа Фібоначчі для розрахунку.
    :type n: int

    :return: Число Фібоначчі за індексом
    :rtype: int
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print("All digits of number 356", get_digits(356))
print("All digits of number 10235", get_digits(10235))

print("The 3rd Fibonacci number:", fibonacci(3))
print("The 5th Fibonacci number:", fibonacci(5))
