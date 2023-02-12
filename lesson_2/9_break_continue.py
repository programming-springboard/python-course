number_to_guess = 42

# while True - нескінченний цикл
while True:
    given_number = int(input("Give me a number: "))

    if given_number == number_to_guess:
        print("You've guessed the number!")
        # Команда break миттєво обриває дію циклу без виконання коду, що далі
        # йде в тілі циклу
        break
    else:
        print("You haven't guessed the number! Try again...")
        # Команда continue переходить одразу до наступної ітерації циклу
        # без виконання коду, що далі йде в тілі циклу
        continue

    print("unreachable code")

print("Game is over")
