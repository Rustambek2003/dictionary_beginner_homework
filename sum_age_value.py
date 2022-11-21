def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    age1 = data[0]['age']
    age2 = data[1]['age']
    return age1 + age2
print(sum_age_values([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]))