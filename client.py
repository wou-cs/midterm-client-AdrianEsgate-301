import requests


def get_programmer_count():
    """
    Return the number of programmers return from the plural programmers API
    :return: An integer indicating the number of programmers in the plural list.
    """
    try:
        base_url = "http://chrisbrooks.pythonanywhere.com"
        response = requests.get(base_url + "/api/programmers")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return len(data.get('programmers', []))


def get_programmer_by_id(pid):
    """
    Return the single programmer referenced by the specified programmer id (pid)
    :param pid: Unique identifier for the programmer to lookup
    :return: A dictionary containing the matched programmer. Return an empty dictionary if not found
    """
    try:
        base_url = "http://chrisbrooks.pythonanywhere.com"
        response = requests.get(base_url + "/api/programmers/{pid}")
        if response.status_code == 404:
            return {}  # Return empty dict if programmer not found
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        for programmer in data.get('programmers', []):
            if programmer.get('id') == pid:
                return {programmer}
    except requests.RequestException:


def get_full_name_from_first(first_name):
    """
    Return the full name of the *first* programmer having the provided first name, concatenating the first and last name with a space between.
    :param first_name:
    :return: A string containing the first and last name of the first programmer in the list of matches.
    """
    try:
        base_url = "http://chrisbrooks.pythonanywhere.com"
        response = requests.get(base_url + "/api/programmers/{first_name}")
        if response.status_code == 404:
            return {}  # Return empty dict if programmer not found
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
    return str(data)
