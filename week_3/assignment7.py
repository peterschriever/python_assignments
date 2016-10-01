import json, requests, sys
from pprint import pprint

# make document api_key.txt in this folder and add your own key
API_KEY = [l for l in open("api_key.txt", 'r')][0].strip()

# get command line arguments
if len(sys.argv) < 2:
    print('Usage: assignment7.py location')
    sys.exit()

# argument 0 is program name
location = ' '.join(sys.argv[1:])

# download JSON data
# url = ='http://api.openweathermap.org/....?
# Notice: using forecast ( API docs: Call 5 day / 3 hour forecast data )
url = "http://api.openweathermap.org/data/2.5/forecast?APPID="+API_KEY+"&q="\
    + location
response = requests.get(url)
response.raise_for_status()

# load JSON data into Python variable
weatherData = json.loads(response.text)
w = weatherData['list']
#pprint(w)

print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
