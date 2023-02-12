# sequence = (1, 2.33, True, False, 42, "foo", 5238, "bar")
sequence = (1, 2.33, True, False, 42, 5238)


for item in sequence:
    if isinstance(item, str):
        print("The first string item in sequence is", item)
        break
else:
    # Якщо цикл завершив своє виконання "природнім" чином, без виклику команди
    # break, то виконається блок else
    print("There are no string items in sequence")
