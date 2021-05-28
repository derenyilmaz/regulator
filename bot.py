import yaml
import telegram
from telegram.ext import Updater
import logging
from telegram.ext import MessageHandler, Filters, CommandHandler

MAX_MESSAGE_LENGTH = 50

config_yaml = open("config.yml")
config = yaml.safe_load(config_yaml)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
bot = telegram.Bot(token=config["token"])
updater = Updater(token=config["token"], use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    context.bot.send_message(chat_id=update.effective_chat.id, text=str(update.effective_chat.id))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def reply(update, context):
    message_text = update.message.text
    if len(message_text.split(" ")) >= MAX_MESSAGE_LENGTH:
        try:
            print(update.message.from_user.username)
        except:
            print("username not found")
        context.bot.send_message(chat_id=update.effective_chat.id, text="your message was too long")
        bot.deleteMessage(chat_id=update.effective_chat.id, message_id = update.message.message_id)
reply_handler = MessageHandler(Filters.text & (~Filters.command), reply)
dispatcher.add_handler(reply_handler)

updater.start_polling()