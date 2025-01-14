def function_with_uncommon_error(data):
    try:
        result = data['key']  # Accessing a key that might not exist
        return result
    except KeyError:
        return None

data = {}
result = function_with_uncommon_error(data)
print(result)  # Output: None

data = {'key': 'value'}
result = function_with_uncommon_error(data)
print(result)  # Output: value