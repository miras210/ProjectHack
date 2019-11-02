import telebot

bot_token = "926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw"
bot = telebot.TeleBot(bot_token)
global logo = open('logo.jpg', 'rb')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы обратились в информационно-справочную службу 109')
    bot.send_photo(message.chat.id,logo)



bot.polling()
