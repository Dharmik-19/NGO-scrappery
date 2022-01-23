import requests
from PIL import Image
from bs4 import BeautifulSoup
from io import BytesIO

search = 'pizza'
#search = input('what you wanan search:')
param = {'q': search}

a = requests.get('http://www.bing.com/images/search', param)


soup = BeautifulSoup(a.text, "html.parser")
div = soup.findAll('a', {'class': 'thumb'})

for i in div:

    img_obj = requests.get(i.attrs['href'])
    print(img_obj.status_code)

    img_obj = requests.get(i.attrs['href'])
    if img_obj.status_code == 200:
        title = i.attrs['href'].split('/')[-1]
        print(title)
        img = Image.open(BytesIO(img_obj.content))
        #img.save("" + title, img.format)