import requests
import json
import urllib
import os
import twint
import csv
from geopy.geocoders import Nominatim
import datetime
import time


def search_twitter(arg, place, input_date):
    """
    This method searches twitter for the argument
    The location is used as a filter for geotag
    The date is used as the END date, the begin date is ONE DAY before
    """
    # configuring location
    geolocator = Nominatim(user_agent="COVID_Tracker")
    location = geolocator.geocode(place)

    # configuring date
    date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    # configuring twint
    c = twint.Config()
    c.Lang = "en"
    c.Search = arg
    c.Since = str(date - datetime.timedelta(days=1))
    c.Until = str(date)
    #c.Geo = str(location.latitude) + "," + str(location.longitude) + ",50mi"
    c.Near = location
    c.Count = True
    c.Hide_output = True
    c.Store_csv = True
    c.Output = "Output"

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


def get_github():
    """
    getting a raw file from github
    """
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/04-12-2020.csv"
    directory = os.getcwd()
    filename = directory + '\somefile.txt'
    r = requests.get(url)
    f = open(filename, 'wb')
    f.write(r.content)


def count_csv():
    """
    count the total tweets scraped by twint
    """
    line_num = 0
    with open("Output/tweets.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            line_num += 1

    return line_num - 1


def process(file_name):
    """
    The function that does most of the work in this program
    Takes the file, scrape twitter for trigger words, outputs the results to
    another compiled csv
    """
    # buffer for each line
    line_buffer = []
    # combined file
    line_stack = []
    # list of words to search twitter
    trigger_list = ["#NoMasks", "#BurnYourMask", "#IWillNotComply",
                    "#OpenAmerica", "#OpenSchools", "#WearAMask", "#WearADamnMask"]
    # reading csv
    with open(os.path.join("Data/States/", file_name), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            line_buffer = row
            print("GATHERING DATA", line_buffer)
            # iterating for each word
            for word in trigger_list:
                search_twitter(
                    arg=word, input_date=row[0], place=capital_dic[row[1]] + "," + row[1])
                # time for the file to save
                time.sleep(3)

                if os.listdir("Output").__contains__("tweets.csv"):
                    # storing the occurances at the end of the line
                    line_buffer.append(count_csv())
                    # clearing storage
                    os.remove("Output/tweets.csv")
                else:
                    line_buffer.append(0)
                    continue

            # stacking the line into the final file
            line_stack.append(line_buffer)
            # avoiding twitter detection
            time.sleep(10)

    # writing output
    with open(os.path.join("Data/States/", "00PROCESSED" + file_name), "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in line_stack:
            writer.writerow(row)

    # clearing storage

    line_buffer.clear()
    line_stack.clear()


# Data for optimizing state searches
# key is the state and value is the capital
capital_dic = {
    'Alabama': 'Birmingham',
    'Alaska': 'Anchorage',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Los Angeles',
    'Colorado': 'Denver',
    'Connecticut': 'Bridgeport',
    'Delaware': 'Wilmington',
    'Florida': 'Jacksonville',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Chicago',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Wichita',
    'Kentucky': 'Louisville',
    'Louisiana': 'New Orleans',
    'Maine': 'Portland',
    'Maryland': 'Baltimore',
    'Massachusetts': 'Boston',
    'Michigan': 'Detroit',
    'Minnesota': 'Minneapolis',
    'Mississippi': 'Jackson',
    'Missouri': 'Kansas City',
    'Montana': 'Billings',
    'Nebraska': 'Omaha',
    'Neveda': 'Las Vegas',
    'New Hampshire': 'Manchester',
    'New Jersey': 'Newark',
    'New Mexico': 'Albuquerque',
    'New York': 'New York City',
    'North Carolina': 'Charlotte',
    'North Dakota': 'Fargo',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Portland',
    'Pennsylvania': 'Philadelphia',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Charleston',
    'South Dakoda': 'Sioux Falls',
    'Tennessee': 'Nashville',
    'Texas': 'Houston',
    'Utah': 'Salt Lake City',
    'Vermont': 'Burlington',
    'Virginia': 'Virginia Beach',
    'Washington': 'Seattle',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Milwaukee',
    'Wyoming': 'Cheyenne'
}

flist = os.listdir("Data/States")
for file in flist:
    if file.__contains__("Florida"):
        process(file)