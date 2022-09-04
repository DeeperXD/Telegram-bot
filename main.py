import telebot
import json
import atexit

import cred

#from types import SimpleNamespace

TOKEN = cred.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)
ACCESSED_PEOPLE = []
GROUP_ID = cred.GROUP_TOKEN


#bot.send_message(GROUP_ID, 'Я врубився')

with open("data.json", 'r') as f:
    data = json.load(f)
    print(f"data loaded: {data}")


class User:
    def __init__(self, username):
        self.username = username
        self.count_of_messages = 1


@bot.message_handler(commands=['top'])
def print_top(message):
    print('command')
    bot.reply_to(message, get_top())


@bot.message_handler(commands=['inactive'])
def print_inactive(message):
    bot.reply_to(message, get_top(True))


@bot.message_handler(commands=['getform'])
def send_about(message):
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

    if str(message.from_user.id) in data:
        data[str(message.from_user.id)]["username"] = message.from_user.username
        data[str(message.from_user.id)]["count_of_messages"] += 1
    else:
        data[str(message.from_user.id)] = User(message.from_user.username).__dict__

    write_data()


def send_data(text):
    bot.send_message(GROUP_ID, text)


def print_commands(message):
    bot.reply_to(message, '/about + текст - додати додаткову інформацію яку бачитимуть всі :)\n'
                          "/get + ім'я та прізвище - інфо про когось (не робить дядь або тьоть)")


def get_top(reverse=False):
    users = list(data.values())
    for i in range(0, len(users)):
        for j in range(i + 1, len(users)):
            if reverse:
                if users[i]["count_of_messages"] > users[j]["count_of_messages"]:
                    users[i], users[j] = users[j], users[i]
            else:
                if users[i]["count_of_messages"] < users[j]["count_of_messages"]:
                    users[i], users[j] = users[j], users[i]
    text = ''
    for i in range(0, len(users)):
        text += f'{users[i]["username"]}: {users[i]["count_of_messages"]}\n'

    return text


def write_data():
    with open("data.json", 'w') as f:
        s = json.dumps(data)
        f.write(s)


def at_exit():
    write_data()


atexit.register(at_exit)

print("bot started")
bot.polling()


