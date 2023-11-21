from helpers import getRandomImageUrl
import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv
load_dotenv()


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    channelId = os.getenv('CHANNEL_ID')

    imageUrl = getRandomImageUrl()
    await bot.send_photo(channelId, imageUrl)


def lambda_handler(event, context):
    asyncio.run(main())


if __name__ == '__main__':
    asyncio.run(main())
