from support import getloc, api_key, icon
import requests


def five_day_forcast():

    city = None
    state = None
    country = None

    if city == None:
        location = getloc()
        city = location[2]
        state = location[3]
        country = location[4]

    forcast_base_url = "https://api.openweathermap.org/data/2.5/forecast?q="
    forcast_complete_url = forcast_base_url + city + \
        ',' + state + ',' + country + '&appid=' + api_key()

    response = requests.get(forcast_complete_url)
    x = response.json()

    jsonfile = open('forcast.json', 'w')
    jsonfile.write(str(x))
    jsonfile.close()

    forcast = []

    for cast in x['list']:
        UTCdate = cast['dt']
        temprature = cast['main']['temp']
        description = cast['weather'][0]['main']
        iconpath = icon(cast['weather'][0]['icon'])
        dt_text = cast['dt_txt']
        lst = [UTCdate, temprature, description, iconpath, dt_text]
        forcast.append(lst)

    return {'forcast': forcast, 'json': str(x)}


if __name__ == '__main__':
    forcast = five_day_forcast()
    print(forcast)
