import telebot
import time

from telebot import types

TOKEN = '926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw'

knownUsers = []
userStep = {}
userNum = {}
userName = {}
userSurname = {}

commands = {
    'start'     : 'This is the beginning of ur journey',
    'help'      : 'Use this in order to see other commands'
}

hideBoard = types.ReplyKeyboardRemove()

def wrong_command(cid):
    bot.send_message(cid, "Hey, bullsh*t you have typed wrong command")
    bot.send_message(cid, "Please try again")

def TelPhone(cid):
    PAns = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Yes = types.KeyboardButton('Yes', request_contact=True)
    No = types.KeyboardButton('No', request_contact=False)
    PAns.row(Yes, No)
    bot.send_message(cid, "Do You trust us ur phone number ?", reply_markup=PAns)

def get_user_data(uid):
    print("[" + str(uid) + "] " + userName[uid] + " " + userSurname[uid] + " " + userNum[uid])
    return userNum[uid]

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected and added \n")
        return 0

def listener(messages):
    for m in messages:
        print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + str(m.text))

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)

def alertBut(m):
    cid = m.chat.id
    time.sleep(2)
    Ans = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Ans.add('Yes', 'No')
    bot.send_message(cid, "Is ur phone number in Telegram real one ?", reply_markup = Ans)
    userStep[cid] = 1


@bot.message_handler(commands=['start'])
def command_help(m):
    cid = m.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        userStep[cid] = 0
        bot.send_photo(cid, open('logo.jpg', 'rb'))
        bot.send_message(cid, "Здравствуйте! Вы обратились в информационно-справочную службу 109")
        alertBut(m)
    else:
        bot.send_message(cid, "I already know you, so what is ur choice ?")
        #action buttons
        

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 1)
def msg_choice(m):
    cid = m.chat.id
    text = m.text
    if text == 'Yes':
        userStep[cid] = 2
        TelPhone(cid)
    elif text == 'No':
        #input your num
        bot.send_message(cid, "Please enter ur phone number")
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 2)
def phone_num(m):
    cid = m.chat.id
    text = m.text
    if text == 'No':
        bot.send_message(cid, "Fuck*ng bastard send ur motherfuck*ng Telegram number")
        TelPhone(cid)
    else:
        wrong_command(cid)

@bot.message_handler(content_types=['contact'])
def phone(m):
    cid = m.chat.id
    text = m.text
    num = m.contact.phone_number
    userNum[cid] = num
    bot.send_message(cid, "Processing ur data ...", reply_markup=hideBoard)
    time.sleep(2)
    bot.send_message(cid, "Enter your name, please")
    userStep[cid] = 3

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 3)
def name(m):
    cid = m.chat.id
    text = m.text
    userName[cid] = text
    bot.send_message(cid, "Processing your data ...")
    time.sleep(1)
    bot.send_message(cid, "Enter your surname, please")
    userStep[cid] = 4

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 4)
def surname(m):
    cid = m.chat.id
    text = m.text
    userSurname = text
    get_user_data(cid)
    bot.send_message(cid, "Thank you for your answers )\nNow wait a sec until new command appears")
    time.sleep(1)


bot.polling()


    