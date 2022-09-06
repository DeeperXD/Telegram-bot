import telebot
import json
import atexit
import database

import cred

TOKEN = cred.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)
ADMINS_ID = []
GROUP_ID = cred.GROUP_TOKEN


@bot.message_handler(commands=['getform'])
def send_form(message):
    photo = open("info.png", "rb")
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types=['photo'])
def on_description(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    message_id = message.message_id
    print(chat_id, message_id)


@bot.message_handler(content_types=["text", "sticker", "photo", "audio", "voice"])
def on_message(message):
    print(message.content_type)
    if message.content_type == "voice":
        bot.send_message(GROUP_ID, "Неперевершений голос!")
    if message.content_type != "text":
        return


def send_data(text):
    bot.send_message(GROUP_ID, text)


def write_data():
    pass


def at_exit():
    write_data()


atexit.register(at_exit)

print("bot started")
bot.polling()


# TODO: реєстрація юзера в системі, а саме, його опис, стать і заповнена форма (це буде по бажанню)
# TODO: підписка на новини та івенти які проводитимуть студенти

# TODO: можливість зареєструватися на певні події
