import requests
import json


response = requests.get('https://www.breakingbadapi.com/api/deaths').text
jdata = json.loads(response)

max_val = jdata[0]
for i in jdata:
    if i['number_of_deaths'] > max_val['number_of_deaths']:
        max_val = i
print(max_val)