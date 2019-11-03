import telebot
import time

from telebot import types

bot_token = "926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw"
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы обратились в информационно-справочную службу 109')
    logo = open('logo.jpg', 'rb')
    bot.send_photo(message.chat.id,logo)
    time.sleep(3)
    bot.send_message(message.chat.id, 'Для дальнейшей работы с ботом нужен доступ к Вашим личным данным')
    time.sleep(1)
    keyboardStart = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Yes = types.KeyboardButton('Yes', request_contact=True)
    No = types.KeyboardButton('No', request_contact=False)
    keyboardStart.row(Yes,No)
    bot.send_message(message.chat.id, 'Согласны передать данные?', reply_markup=keyboardStart)
    
    keyboardStart=telebot.types.ReplyKeyboardRemove(selective=True)
    bot.send_message(message.chat.id, message, reply_markup=keyboardStart)

bot.polling()
