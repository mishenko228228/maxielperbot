from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('TOKEN')

def start(update, context):
    update.message.reply_text('Привет! Я MaxHelperBot.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    PORT = int(os.environ.get('PORT', '8443'))
    APP_NAME = 'maxielperbot'  # ← замени на имя твоего Render приложения

    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=TOKEN
    )
    updater.bot.set_webhook(f"https://{APP_NAME}.onrender.com/{TOKEN}")

    updater.idle()

if name == '__main__':
    main()