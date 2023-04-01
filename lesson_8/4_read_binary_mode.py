with open("file.txt", "rb") as file:
    file_text_as_bytes = file.read()

print("Type of file text:", type(file_text_as_bytes))
print("=" * 25)
print(file_text_as_bytes)
