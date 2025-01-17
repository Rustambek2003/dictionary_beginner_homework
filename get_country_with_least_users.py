def get_country_with_least_users(data:list) -> str:
    """
    Return the country with the least users

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The country with the least users
    """
    country1 = data[0]['country']
    country2 = data[1]['country']
    if len(country1) < len(country2):
        return country1
    else:
        return country2
print(get_country_with_least_users([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]))