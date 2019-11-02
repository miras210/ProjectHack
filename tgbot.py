import telebot

from telebot import types

bot_token = "926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы обратились в информационно-справочную службу 109')
    logo = open('logo.jpg', 'rb')
    bot.send_photo(message.chat.id,logo)
    bot.send_message(message.chat.id, 'Для дальнейшей работы с ботом нужен доступ к Вашим личным данным')
    markup = types.ReplyKeyboardMarkup(row_width=2)
    Yes = types.KeyboardButton('Yes')
    No = types.KeyboardButton('No')
    markup.add(Yes, No)
    bot.send_message(message.chat.id, "Согласны передать данные?:")

bot.polling(none_stop=True, interval=0, timeout=3)
