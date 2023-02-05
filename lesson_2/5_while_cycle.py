sequence = ("First", "Second", "Third")

counter = 0

# Для повторного виконання певних операцій використовуються цикли
# Найпримітивніший варіант циклу - цикл while, що виконується, поки вказана
# після ключового слова умова при перевірці на істину повертає значення True
while counter < len(sequence):
    print(f"Sequence item at index {counter}: {sequence[counter]}")
    counter += 1  # цей запис еквівалентний counter = counter + 1
