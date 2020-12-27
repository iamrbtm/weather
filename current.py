from database import insert_data_current
import requests, time
import socket
from datetime import datetime, timedelta
from support import getloc, api_key
from urllib.request import urlopen


def current_weather():
    """Weather Getter
    get weather conditions for current city

    Returns Dictionary:
        [0]temp:       current temperature
        [1]iconpic:    icon for current weather conditions
        [2]city:       current city (from getloc)
        [3]lat:        latatude of city ping (from getloc)
        [4]lon:        longatude of city ping (from getloc)
        [5]sunrise:    time of sunrise
        [6]sunset:     time of sunset
    """

    city = None
    lat = None
    lon = None

    if city == None:
        location = getloc()
        city = location[2]
        lat = location[0]
        lon = location[1]

    weather_base_url = "http://api.openweathermap.org/data/2.5/weather?"

    weather_complete_url = weather_base_url + 'lat=' + \
        lat + '&lon=' + lon + '&appid=' + api_key()

    response = requests.get(weather_complete_url)
    x = response.json()

    jsonfile = open('current.json', 'w')
    jsonfile.write(str(x))
    jsonfile.close()

    temp = round((((x['main']['temp']-273.150)*1.8)+32))

    iconcode = x['weather'][0]['icon']
    iconpic = 'img/icons/' + iconcode + '.png'

    sunrise = (datetime.utcfromtimestamp(
        x['sys']['sunrise'])-timedelta(hours=8)).strftime('%I:%M %p')

    sunset = (datetime.utcfromtimestamp(
        x['sys']['sunset'])-timedelta(hours=8)).strftime('%I:%M %p')

    insert_data_current(temp, iconpic, city, lat, lon, sunrise, sunset)

    return {'temp': temp, 'icon': iconpic, 'city': city, 'lat': lat, 'lon': lon, 'sunrise': sunrise, 'sunset': sunset}


if __name__ == '__main__':
    cur_weather = current_weather()
    secondsFromEpoch = time.time()
    timeObj = time.localtime(secondsFromEpoch)
    print("Execution Time: %d/%d/%d %d:%d:%d" % ( timeObj.tm_mon, timeObj.tm_mday, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec), end='\n')
    print("Computer: " + socket.gethostname() + " | " + socket.gethostbyname(socket.gethostname()))
    print(cur_weather)
