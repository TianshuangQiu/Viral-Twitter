import requests
import json
import urllib
from os import getcwd
import twint
from geopy.geocoders import Nominatim



geolocator = Nominatim(user_agent="COVID_Tracker")
location = geolocator.geocode("Fairfax, Virginia")
print(location.latitude, location.longitude)
c = twint.Config()
c.Lang = "en"
c.Search = "#coronavirus"
c.Since = "2020-7-10 0:0:0"
c.Geo = str(location.latitude) + "," + str(location.longitude) + ", 5km"
c.Count = True
c.Store_csv = True
c.Output = "test"

twint.run.Search(c)


with urllib.request.urlopen("https://geo.fcc.gov/api/census/area?lat=38.8462236&lon=-77.3063733&format=json") as url:
    data = json.loads(url.read().decode())
    print(data)

print(json.dumps(data, indent=4, sort_keys=True))

print(data['results'][0]['state_fips'])
print(data['results'][0]['county_fips'])
print(data['results'][0]['county_name'])


url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/04-12-2020.csv"
directory = getcwd()
print(directory)
filename = directory + 'somefile.txt'
r = requests.get(url)

f = open(filename, 'wb')
f.write(r.content)
