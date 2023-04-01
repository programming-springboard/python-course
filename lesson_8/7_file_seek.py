with open("file.txt", "r") as file:
    data = file.read()
    file.seek(0)
    data2 = file.read()


print(f"{data=}")
print(f"{data2=}")
