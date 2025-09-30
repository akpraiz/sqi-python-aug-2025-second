import requests
from typing import List

JSONPLACEHOLDER_USERS = "https://jsonplaceholder.typicode.com/users"

def fetch_user_data() -> List[str]:
    """
    Fetches users from JSONPlaceholder and returns a list of user names.
    Raises requests.HTTPError on bad status codes.
    """
    resp = requests.get(JSONPLACEHOLDER_USERS, timeout=10)
    resp.raise_for_status()  # raises HTTPError
    data = resp.json()

    return [user.get("name", "") for user in data]
