import telebot

bot_token = "926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Вы обратились в информационно-справочную службу 109')
    
@bot.message_handler(commands = ['help'])
def start_message(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, message.text)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text == 'Мирас':
        bot.send_message(message.chat.id, 'Пидарас')
    else:
        bot.send_message(message.chat.id, bot.id)
        bot.send_message(message.chat.id, bot.first_name)
        bot.send_message(message.chat.id, bot.last_name)
        bot.send_message(message.chat.id, bot.username)

bot.polling()
