import requests
import os
from datetime import datetime
import json

api_key = "7bde006b0bdd37843329696e6289ec40"
city_zip = "80501"
city = "Longmont"
city_id = "5579276"
uri = "api.openweathermap.org/data/2.5/weather?"
url = "http://" + uri + "id=%s&units=imperial&APPID=%s" % (city_id, api_key)
FMT = "%Y-%m-%d %H:%M:%S.%f"

datoom = requests.get(url)

print datoom.json()


def populate_file(data_file):
    """Retrieve the data and sticks it in the file."""
    current_time = datetime.now()
    data_file.write(current_time)
    #get system time
    #write to file
    #get data
    #write to file
    return "other things"


""" Check time in file and either retrieve data
    from remote or return data already in file 
"""
def process_file(data_file):
    current_time = datetime.now()
    file_time = data_file
    # if file is out of date, make sure data is overwritten
    tdelt = datetime.strptime(current_time, FMT) - datetime.strptime(file_time, FMT)
    if tdelt.total_seconds < 900:
        data = open(data_file, 'r+').firstline()[""]
    else:
        data = populate_file(data_file)

    return "things!"

# Check to see if file exists. If it doesn't create it
''' Doc String '''
def check_data_file():
    if os.path.isfile("weather_data.txt"):
        data_file = open("weather_data.txt", 'r')
        data = process_file(data_file)
        data_file.close()
        return data
    else:
        data_file = open("weather_data.txt", 'w')
        populate_file(data_file)
        data = process_file(data_file)
        data_file.close()
        return data

