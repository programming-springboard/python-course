def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(F"{key}: {value}")


def replace_dict_keys(original_dict, **mapping):
    result = original_dict.copy()
    for old_key_name, new_key_name in mapping.items():
        if old_key_name in original_dict:
            value = result.pop(old_key_name)
            result[new_key_name] = value
    return result


print_kwargs(a=1, b=42, c="foo", any_given_name="any_given_value", sample_value={"key": "value"})


d = {"a": 1, "b": 2, "c": 3}
print("Original dict:", d)
print("Dict after key replacement:", replace_dict_keys(d, b="f", non_existing_key="c"))
