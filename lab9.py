Question4: Write a function that recursively searches for a key in a nested dictionary and returns its value.
    
    nested_dict = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 4
        }
    },
    'g': 5
}

key_to_search = 'f'
result = recursive_dict_search(nested_dict, key_to_search)

if result is not None:
    print(f"The value of key '{key_to_search}' is: {result}")
else:
    print(f"Key '{key_to_search}' not found in the nested dictionary.")
