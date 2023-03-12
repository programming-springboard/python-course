def print_numbers(*args):
    print("The given function args array:", args)
    print("Type of args:", type(args))
    first_argument = args[0]
    print("The first argument is", first_argument)


def add_all(*nums):
    result = 0
    for num in nums:
        result += num
    return result


print_numbers(1, 2, 3, 4, 5)
print("The sum of numbers is", add_all(1, 2, 3, 4, 5))
