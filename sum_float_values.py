def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    ans = 0
    for i in data.values():
        if type(i) == float:
            ans += i
    return ans
print(sum_float_values({'a': 1, 'b': 2.5, 'c': 3.0}))