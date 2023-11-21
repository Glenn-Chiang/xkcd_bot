import requests
from bs4 import BeautifulSoup

def getRandomImageUrl():
    res = requests.get('https://c.xkcd.com/random/comic/')
    pageSource = BeautifulSoup(res.text, "html.parser")
    imageElement = pageSource.select_one("#comic>img")
    imageUrl = 'https:' + imageElement.get('src')
    return imageUrl
