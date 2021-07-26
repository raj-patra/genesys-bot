from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from bot import GenesisBot
import os

PORT = os.environ.get('PORT', 5000)
AUTH = os.environ.get('BOT_TOKEN')
HOOK = 'https://genesys-bot.herokuapp.com/'

def app():
    genesis = GenesisBot()
    updater = Updater(AUTH, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", genesis.start, filters = (Filters.command | Filters.regex(r'^/start@[\w.]+$'))))
    dp.add_handler(CommandHandler("help", genesis.help, filters = (Filters.command | Filters.regex(r'^/menu@[\w.]+$'))))
    dp.add_handler(CommandHandler("dev", genesis.dev, filters = (Filters.command | Filters.regex(r'^/dev@[\w.]+$'))))

    dp.add_handler(InlineQueryHandler(genesis.inline_query, pass_chat_data=True))
    dp.add_handler(CallbackQueryHandler(genesis.callback_query))

    dp.add_error_handler(genesis.error)

    updater.start_webhook(listen='0.0.0.0', port=PORT, webhook_url=HOOK)
    updater.idle()

if __name__ == '__main__':
    app()