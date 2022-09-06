import telebot
from telebot import  types

import json
import atexit
import database

import cred

TOKEN = cred.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)
ADMINS_ID = []
GROUP_ID = cred.GROUP_TOKEN


@bot.message_handler(commands=['start', 'info']) # початок діалогу з ботом
def send_start_message(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        types.InlineKeyboardButton("Зареєструватися", callback_data="register"),
        types.InlineKeyboardButton("Інфо про реєстрацію", callback_data='register info'),
        types.InlineKeyboardButton("Діскорд сервер", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    )

    bot.send_message(message.chat.id, 'Привіт, я бот ФІКТ, і я допоможу тобі бути вкурсі новин'
                                      ' та познайомитися з новими друзями'
                                      ', за допомогою команд ти зможеш зареєструвати себе в системі знаймств'
                                    , reply_markup=markup)


@bot.callback_query_handler(lambda query: query.data == 'register')
def register(query): # реєстрація
    bot.send_message(query.message.chat.id, 'Congrats you started register')

    # потрібно описати етапи реєстрації


@bot.callback_query_handler(lambda query: query.data == 'register info')
def register(query):  # реєстрація
    bot.send_message(query.message.chat.id, 'Після реєстрації можна добавити додаткову інформцію про себе')

    # потрібно описати етапи реєстрації

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



# Привіт, я бот ФІКТ, і я допоможу тобі бути вкурсі новин, та познайомитися з новими друзями
# за допомогою команд ти зможеш зареєструвати себе в системі знаймств,
# не переживай ці дані ми ніяк не застосовуємо, це просто твоя анкета)
# напиши команду /set description і після цього відправ короткий опис про себе)
# напиши команду /set form і після цього відправ заповнену форму

# лінк на наш сервер дс
# лінк на телеграм группу







# TODO: реєстрація юзера в системі, а саме, його опис, стать і заповнена форма (це буде по бажанню)
# TODO: підписка на новини та івенти які проводитимуть студенти

# TODO: можливість зареєструватися на певні події
