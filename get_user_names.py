def get_user_names(data:list, country:str) -> list:
    """
    Return a list of users with a given country

    Args:
        data (dict): A dictionary of values
        country (str): The country to search for
    Returns:
        list: A list of users with the given country
    """
    country1 = data[0]['country']
    country2 = data[1]['country']
    if country1 == country:
        return [data[0]["name"]]
    elif country2 == country:
        return [data[1]["name"]]
print(get_user_names([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"USA"))