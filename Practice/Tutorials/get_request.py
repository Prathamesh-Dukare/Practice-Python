import requests
import queue
url='https://www.metaweather.com/api/location/2295420/'
obj=requests.get(url)
print(obj.text)