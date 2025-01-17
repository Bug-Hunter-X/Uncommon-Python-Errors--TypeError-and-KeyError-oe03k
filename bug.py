def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return float('inf')
    except TypeError:
        return None

# This will trigger the uncommon TypeError
result = function_with_uncommon_error(10, '2')
print(result)  # Output: None

#Another example of a less common error
my_dict = {'a': 1, 'b': 2}
print(my_dict['c']) # KeyError: 'c'