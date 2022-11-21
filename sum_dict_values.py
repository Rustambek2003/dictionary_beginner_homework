def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    ans = 0
    for i in data.values():
        ans += i
    return ans
print(sum_dict_values({'a': 1, 'b': 2, 'c': 3}))