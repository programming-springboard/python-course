sequence = (42, "String item", True)

# Для отримання доступу до елементів кортежа за їх індексом використовується
# оператор квадратні дужки [], аргументом якого слугує бажаний індекс.
# Індексація елементів послідовності в Python починається з нуля.
print("First item of sequence", sequence[0])
print("Second item of sequence", sequence[1])
print("Third item of sequence", sequence[2])

# В Python також є певний трюк з отриманням значення за негативним індексом. В
# такому випадку Python буде намагатись взяти i-тий елемент з кінця (на 
# прикладі нижче - перший елемент з кінця)
print("Last item of sequence", sequence[-1])
