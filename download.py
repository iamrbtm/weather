from io import BytesIO
from PIL import Image
import requests
import os

files = ['01d', '01n', '02d', '02n', '03d', '03n', '04d', '04n', '09d',
         '09n', '10d', '10n', '11d', '11n', '13d', '13n', '50d', '50n', ]
exts = ['.png', '@2x.png']
url = 'https://openweathermap.org/img/wn/'

for file in files:
    for ext in exts:
        if not os.path.isfile(os.path.join(os.getcwd(), 'forcast/', file + ext)):
            r = requests.get(url + file + ext)
            im = Image.open(BytesIO(r.content))
            im.save('forcast/' + file + ext)
            print('Downloaded ' + file + ext)
        else:
            print(file + ext + ' already downloaded')
