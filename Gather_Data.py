import requests
import json
import urllib
from os import getcwd
import twint
from geopy.geocoders import Nominatim
import datetime


def search_twitter(arg, place, date):
    """
    This method searches twitter for the argument
    The location is used as a filter for geotag
    The date is used as the END date, the begin date is ONE DAY before
    """
    geolocator = Nominatim(user_agent="COVID_Tracker")
    location = geolocator.geocode(place)
    print(location.latitude, location.longitude)
    # configuring twint
    c = twint.Config()
    c.Lang = "en"
    c.Search = arg
    c.Since = date - datetime.timedelta(days=1)
    c.Until = date
    c.Geo = str(location.latitude) + "," + str(location.longitude) + ", 5km"
    c.Count = True
    c.Store_csv = True
    c.Output = "test"

    twint.run.Search(c)


def reverse_geocode(lat, lon):
    """
    Searching the state and county when given latitude and longitude
    """
    with urllib.request.urlopen("https://geo.fcc.gov/api/census/area?lat=" + lat + "&lon=" + lon + "&format=json") as url:
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
