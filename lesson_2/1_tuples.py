# Для позначення переліків (масивів) даних НЕЗМІННОЇ довжини в Python
# використовується тип даних tuple (кортеж).
sequence = (1, 2, 3)
print("The sequence items are", sequence)
print("The sequence type is", type(sequence))

# Для отримання довжини певної послідовності в Python використовується функція
# len()
print("The sequence length is", len(sequence))

# Підказка: функція len() також може використовуватися, аби отримати кількість
# символів певної строки
print('The length of "abcd" is', len("abcd"))

# Кортежі також можна ініціалізувати і без дужок (). За замовчуванням, перелік
# декількох елементів через кому , Python сприймає за кортеж даних
another_sequence = 3, 2, 1
print("Another sequence items are", another_sequence)
print("Another sequence type is", type(another_sequence))

# Елементами кортежу так само можуть бути інші кортежі
nested_tuples = (
    (1, 2),
    ("Three", "Four"),
    (5.0, 6.0),
)
print("Nested tuples:", nested_tuples)
