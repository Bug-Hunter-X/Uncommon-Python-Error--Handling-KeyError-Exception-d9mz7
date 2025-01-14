def function_with_uncommon_error(data):
    try:
        result = data['key']  # Accessing a key that might not exist
        return result
    except KeyError:
        return None  # Handle the exception by returning None

data = {}
result = function_with_uncommon_error(data)
print(result)  # Output: None

data = {'key': 'value'}
result = function_with_uncommon_error(data)
print(result)  # Output: value

#Alternative solution using the .get() method:

def function_with_get_method(data):
    return data.get('key') #returns None if key is not found

data = {}
result = function_with_get_method(data)
print(result) #Output: None

data = {'key':'value'}
result = function_with_get_method(data)
print(result) #Output: value