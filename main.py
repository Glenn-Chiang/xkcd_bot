import os
import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()


def getRandomImageUrl():
    res = requests.get('https://c.xkcd.com/random/comic/')
    pageSource = BeautifulSoup(res.text, "html.parser")
    imageElement = pageSource.select_one("#comic>img")
    imageUrl = 'https:' + imageElement.get('src')
    return imageUrl



async def main():
    print("Started")
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    channelId = os.getenv('CHANNEL_ID')

    imageUrl = getRandomImageUrl()
    print(imageUrl)
    await bot.send_photo(channelId, imageUrl)


def lambda_handler(event, context):
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())
