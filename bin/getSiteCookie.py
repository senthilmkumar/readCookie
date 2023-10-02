import requests
import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

os.chdir(__location__)
os.system('clear')


print("Running through gihub actions")

# URL of the website you want to check
#url = 'https://google.com'

with open('../config/sites.json') as f:
    data = json.load(f)

for site, url in data.items():
    print(f"{site}: {url}")

    # Send an HTTP GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract and print the cookies from the response
        cookies = response.cookies
        for cookie in cookies:
            print(f"Cookie Name: {cookie.name}")
            print(f"Cookie Value: {cookie.value}")
    else:
        print(f"Failed to fetch the website. Status code: {response.status_code}")

