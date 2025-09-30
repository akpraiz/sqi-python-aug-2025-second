import requests

from bs4 import BeautifulSoup

url = "https://www.jumia.com.ng"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Oh no! Something went wrong. Maybe check your internet connection? More details:")
    print(e)
else:
    soup = BeautifulSoup(response.text, 'html.parser')
    if response.status_code == 200:
        with open("jumia-home.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
    else:
        print(f"Unexpected response: {soup.prettify()}")