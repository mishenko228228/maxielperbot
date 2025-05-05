from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('TOKEN')

def start(update, context):
    update.message.reply_text('Привет! Я MaxHelperBot.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()