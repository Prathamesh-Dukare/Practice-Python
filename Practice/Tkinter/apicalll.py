import requests

url = "https://www.metaweather.com/api/location/search/?query=san"


# Use the library to perform an HTTP GET request to the URL

response = requests.get(url)


# Print out the data

print(response.text)

