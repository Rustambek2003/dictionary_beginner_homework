def find_max_key(data: dict) -> int:
    """
    Return the maximum key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max = 0
    for i in data.keys():
        if max < i:
            max = i
    return max
print(find_max_key({1:'a', 12:'b', 3: 'c'}))