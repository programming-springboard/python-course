import json

my_dict = {
    "first_name": "Olexandra",
    "age": 26,
    "status": "Prettiest woman in the world",
}

data_to_write = json.dumps(my_dict)
print("type of data_to_write", type(data_to_write))
print(f"{data_to_write=}")
parsed_data = json.loads(data_to_write)
print("type of parsed_data", type(parsed_data))
print(f"{parsed_data=}")

with open("file.json", "w") as file:
    file.write(data_to_write)

# with open("file.json", "w") as file:
#     json.dump(data_to_write, file, indent=2)
#
# with open("file.json", "r") as file:
#     data_from_file = json.load(file)