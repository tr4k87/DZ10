import telebot
from telebot import types
bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=['start'])
def category(message):
    bot.send_message(message.from_user.id, 'Введи выражение:')
    bot.register_next_step_handler(message, calc)
    

def calc(message):
    spy(message)
    value = message.text
    value = str(eval(value))
    bot.send_message(message.from_user.id, value)

def spy(message):
    file = open('db.csv', 'a')
    file.write(f'{message.from_user.first_name}, {message.from_user.id}, {message.text}\n')
    file.close()

bot.polling(none_stop=True, interval=0)
