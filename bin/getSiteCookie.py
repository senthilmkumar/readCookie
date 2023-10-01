import requests

# URL of the website you want to check
url = 'https://google.com'

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
