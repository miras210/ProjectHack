import telebot

from telebot import types

bot_token = "926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw"
bot = telebot.TeleBot(bot_token)
keyboardStart = telebot.types.ReplyKeyboardMarkup(True)
Yes = types.KeyboardButton('Yes', request_contact=True)
No = types.KeyboardButton('No', request_contact=False)
keyboardStart.row(Yes,No)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы обратились в информационно-справочную службу 109')
    logo = open('logo.jpg', 'rb')
    bot.send_photo(message.chat.id,logo)
    bot.send_message(message.chat.id, 'Для дальнейшей работы с ботом нужен доступ к Вашим личным данным')
    bot.send_message(message.chat.id, 'Согласны передать данные?:', reply_markup=keyboardStart)
    reply_markup=telebot.types.ReplyKeyboardRemove(remove_keyboard=True)

bot.polling(none_stop=True, interval=0, timeout=3)
