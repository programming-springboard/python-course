def add(a, b=2):
    return a + b


result_1 = add(3)
result_2 = add(3, 3)
result_3 = add(2)

print("Result of 3 + DEFAULT_FUNCTION_VALUE(2) =", result_1)
print("Result of 3 + 3 =", result_2)
print("Result of 2 + 2 =", result_3)