
def get_user_names_with_age_range_and_country(data:list, min_age:int, max_age:int, country:str) -> list:
    """
    Return a list of users with a given age range and country.

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
        country (str): The country to search for
    Returns:
        list: A list of users with the given age range and country
    """
    age1 = data[0]['age']
    age2 = data[1]['age']
    if min_age<age1<max_age:
        return [data[0]["name"]]
    elif max_age<age2<max_age:
        return [data[1]["name"]]
print(get_user_names_with_age_range_and_country([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}],20,30,"USA"))