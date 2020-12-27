from io import BytesIO
from PIL import Image
import requests
import os, socket


def icon(icon_number, size=''):
    file = None

    url = 'https://openweathermap.org/img/wn/'

    if size != '':
        iconsize = '@2x'
    else:
        iconsize = ''

    filename = str(icon_number + iconsize + '.png')
    file_dir = os.path.join(os.getcwd(), "forcast")
    file = os.path.join(file_dir, filename)

    #check to see if directory exists
    if os.path.isdir(file_dir):
        pass
    else:
        os.mkdir(file_dir)

    # check to see if file exists
    if os.path.isfile(file):
        return file
    else:
        r = requests.get(url + icon_number + iconsize + '.png')
        im = Image.open(BytesIO(r.content))
        im.save(file)

        return file


def getloc():
    """get location based on current ip address

    Returns:
        lat: latatude of pinged ip address
        lon: longatude of pinged ip address
        city: name of city based on ip address
        state: name of state of pinged ip address
        country: country of pinged ip address
    """
    res = requests.get('https://ipinfo.io/')
    data = res.json()

    location = data['loc'].split(',')
    city = data['city']
    lat = location[0]
    lon = location[1]
    state = data['region']
    country = data['country']
    ip = data['ip']

    return [lat, lon, city, state, country, ip]


def api_key():
    api_key = 'd82b0279071b7dbbf121b243ff6dfa62'
    return api_key


if __name__ == '__main__':
        location = getloc()
        print(location)

    # file = icon('50n', 2)
    # print(file)
