first_tuple = (1, 2, 3)
second_tuple = (4,)  # також можливо: second_tuple = tuple(4)

# В Python можливо проводити ще деякі операції над кортежами. Наприклад, при
# скаладанні двох кортежів отримаємо третій кортеж, який буде включати
# послідовно елементи перших двух
print(f"Sum of tuples:", first_tuple + second_tuple)

# Також, за допомогою оператора множення можна одразу створювати великий кортеж
# заповнений якимись даними. Це може бути корисно, коли розмір кортежу
# заздалегідь невідомий і визанчається в ході виконання програми. Таким чином
# можливо "зарезервувати" памʼять масиву, аби потім заповнити його даними.
print("Tuple multiplication", second_tuple * 10)

empty_tuple = ()   # також можливо: empty_tuple = tuple()

# Пустий кортеж при перевірці на істину буде завджи повертати значення False.
# Кортеж, що має принаймні одне значення всередині, при перевірці на істину
# буде завджи давати результат False.
print("Casting tuple to boolean:", bool(second_tuple))
print("Casting empty tuple to boolean", bool(empty_tuple))

if not empty_tuple:
    print("The tuple is empty. Please, fill it with values")
