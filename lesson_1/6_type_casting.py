# Функція input() в результаті свого виконання повертає значення типу str

# Деколи, для корректної роботи програми треба привести значення типу str до
# одного з числових типів (int, float), аби мати можливість виконувати над
# ними математичні операції.

# Для цього, результат виконання input() треба передати до вбудованої функції 
# int() або float()

# first_number = input("First number: ")
# second_number = input("Second number: ")
#
# print("The result of addition:", first_number - second_number)

raw_first_number = input("Enter first number: ")
raw_second_number = input("Enter second number: ")

first_number = int(raw_first_number)
second_number = int(raw_second_number)

# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter second number: "))

print(f"{first_number} + {second_number} = {first_number + second_number}")

# Теж саме працює і з функцією float(). Зверни увагу, що при введені з
# клавіатури, дробне значення від цілого слід передавати за допомогою крапки .
# В іншому випадку, якщо використати, до прикладу, кому, значення не буде
# прийнято, а інтерпретатор Python сповістить про помилку обробки даних.

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# print(f"{first_number} + {second_number} = {first_number + second_number}")
