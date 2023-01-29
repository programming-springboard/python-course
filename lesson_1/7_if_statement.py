# Для перевірки логічних виразів в Python використовується оператор if:

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print("The first number is bigger!")
elif first_number == second_number:
    print("The numbers are equal!")
else:
    print("The second number is bigger!")

# Резуоьтатами виконання логічних операцій є тип bool (від англ. boolean). 
# В Python є двів будованих змінні типу bool: True і False

# if True:
#     print("if True proceeded!")

# if False:
#     print("if False proceeded!")
# else:
#     print("if False did not proceed")

# print("Type of True:", type(True))
# print("Type of False:", type(False))
# print("Type of boolean expression:", type(first_number > second_number))

# Можна також проводити декілька логічних операцій за раз, поєднуючі їх
# логічними "і", "або", "ні"

# if first_number > second_number and first_number != 3:
#     print("First number is bigger AND it is not equal to 3!")
# elif first_number > second_number or first_number != 3:
#     print("First number is bigger OR it is not equal to 3!")
# elif not first_number > second_number:
#     print("First number is not bigger!")

# Логічними операторами є:
#   >   більше
#   <   менше
#   >=  більше або дорівнює
#   <=  менше або дорівнює 
#   ==  дорівнює
#   !=  не дорівнює
#   and логічне 'i'
#   or  логічне 'або'
#   not логічне 'ні'
