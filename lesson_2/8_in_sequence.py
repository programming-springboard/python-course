sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
number = int(input("Please, enter a natural number: "))

# Для того, аби перевірити чи входить якийсь елемент до певної послідовності
# використовується ключове слово in
if number in sequence:
    print("The given number is in Fibonacci sequence!")
else:
    print("The given number is not in Fibonacci sequence!")
