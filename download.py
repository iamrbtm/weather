from io import BytesIO
from PIL import Image
import requests

files = ['01d', '01n', '02d', '02n', '03d', '03n', '04d', '04n', '09d', '09n', '10d', '11d', '11n', '13d', '13n', '50d', '50n',]
url = 'https://openweathermap.org/img/wn/'

for file in files:
    r = requests.get(url + file + '@2x.png')
    im = Image.open(BytesIO(r.content))
    im.save('forcast/' + file + '@2x.png')

    r = requests.get(url + file + '.png')
    im = Image.open(BytesIO(r.content))
    im.save('forcast/' + file + '.png')
    
    print ('Done with ' + file)