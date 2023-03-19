from my_module import my_super_cool_print_function
from my_package.my_inner_module import fibonacci
from my_package import my_other_inner_module


def main():
    my_super_cool_print_function("2 + 2 = 4")

    fibonacci_10 = fibonacci(10)
    my_super_cool_print_function(f"Fibonacci number at index 10 is {fibonacci_10}")

    digits = my_other_inner_module.get_digits(12345)
    my_super_cool_print_function(f"Digits of number 12345 are {digits}")


if __name__ == "__main__":
    main()
