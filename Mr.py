from urllib import request
import requests

import json 
import sys
zip = input("what is your city or zipcode?: ")
try:
    with open ('API-key') as f:
        key = f.readline
except:
    print ('Add your API key from visual crossing to a file named "API-key"')
    sys.exit()
data = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{zip}?unitGroup=us&key={key}&contentType=json')

results = json.loads(data.text)
print (f"Todays High in {zip} is:{results['days'][0]['tempmax']}")
print (f"Todays low in {zip} is: {results['days'][0]['tempmin']}")
#this is my dev branch#