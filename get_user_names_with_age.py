def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    age1 = data[0]['age']
    age2 = data[1]['age']
    if age1 == age:
        return [data[0]['name']]
    elif age2 == age:
        return [data[1]['name']]
print(get_user_names_with_age([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}],27))
