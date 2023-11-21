from helpers import getRandomImageUrl
import asyncio
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv
load_dotenv()


async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('Enter /xkcd to get a random xkcd comic')


async def sendImage(update: Update, context: CallbackContext):
    imageUrl = getRandomImageUrl()
    await update.message.reply_photo(imageUrl)


async def main(event):
    app = Application.builder().token(os.getenv('BOT_TOKEN')).build()

    app.add_handler(CommandHandler('xkcd', sendImage))

    await app.initialize()
    update = Update.de_json(data=json.loads(event['body']), bot=app.bot)
    await app.process_update(update=update)


def lambda_handler(event, context):
    asyncio.run(main(event))


if __name__ == '__main__':
    main()
